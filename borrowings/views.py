from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import UserAccount
from books.models import Book
from .models import Borrowing
from django.contrib import messages
from bookomari.utils import send_email
from django.views.generic import ListView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@login_required
def place_borrowing(req):
  account_id = req.GET.get('account_id')
  book_slug = req.GET.get('book_slug')

  account = UserAccount.objects.get(account_id = account_id)
  book = Book.objects.get(slug = book_slug)

  if account.balance >= book.borrowing_price:

    account.balance -= book.borrowing_price
    account.save()

    Borrowing.objects.create(
      account = account,
      book = book,
      borrowing_price = book.borrowing_price,
      balance_after_borrowing = account.balance,
      status = 'borrowed'
    )

    messages.success(req, "Book borrowed")

    send_email(
      "Confirmation of borrowing",
      book.borrowing_price,
      account.user,
      'borrowings/borrow_confirm_mail.html'
    )

    return redirect('book-detail', book_slug = book.slug)
  else:
    messages.info(req, "Insufficience balance. Deposit more to borrow book.")

    return redirect('book-detail', book_slug = book.slug)

@method_decorator(login_required, name = 'dispatch')
class BorrowingReportView(ListView):
  template_name = 'borrowings/borrowing_report.html'
  model = Borrowing
  context_object_name = 'borrowing'

  def get_queryset(self):
    user_account = self.request.user.account

    querySet = super().get_queryset().filter(account = user_account)
    return querySet
    
@method_decorator(login_required, name = 'dispatch')
class ReturnBorrowedBookView(View):
  def get(self, req, borrow_id):
    borrowing = get_object_or_404(Borrowing, id = borrow_id)
    user_account = self.request.user.account

    user_account.balance += borrowing.borrowing_price
    user_account.save()

    borrowing.status = 'returned'
    borrowing.save()
    
    messages.success(req, 'Book returned')
    return redirect('borrowing-report')