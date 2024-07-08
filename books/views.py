from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import BookForm
from .models import Book
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

  return render(req, 'books/book_detail.html', {
    'book': book
  })