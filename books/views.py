from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import BookForm
from .models import Book
from reviews.forms import ReviewForm
from reviews.models import Review
from borrowings.models import Borrowing
from django.contrib import messages
from django.template.defaultfilters import slugify

# Create your views here.
@method_decorator(login_required, name = 'dispatch')
class AddBookView(CreateView):
  template_name = 'books/add_book.html'
  form_class = BookForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    book = form.save(commit = False)
    book.slug = slugify(book.title)
    book.save()

    messages.success(self.request, "Book added")

    return super().form_valid(form)

def book_detail(req, book_slug):
  book = Book.objects.get(slug = book_slug)
  reviews = Review.objects.filter(user = req.user, book = book)
  borrowings = Borrowing.objects.filter(account = req.user.account, book = book)

  if req.method == 'POST':
    form = ReviewForm(req.POST)

    if form.is_valid():
      new_form = form.save(commit = False)
      new_form.user = req.user
      new_form.book = book
      new_form.save()
      messages.success(req, "Review added.")
      return redirect('book-detail', book_slug = book.slug)
  else:
    form = ReviewForm()

  return render(req, 'books/book_detail.html', {
    'book': book,
    'reviews': reviews,
    'review_form': form,
    'borrowings': borrowings
  })