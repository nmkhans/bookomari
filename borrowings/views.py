from django.shortcuts import render, redirect
from accounts.models import UserAccount
from books.models import Book
from .models import Borrowing
from django.contrib import messages
from bookomari.utils import send_email


# Create your views here.
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

