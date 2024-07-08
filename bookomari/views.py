from django.shortcuts import render
from categories.models import Category
from books.models import Book

def home(req, category_slug = ""):
  categories = Category.objects.all()

  if not category_slug:
    books = Book.objects.all()
  else:
    category = Category.objects.get(slug = category_slug)
    books = Book.objects.filter(categories = category)
  

  return render(req, 'index.html', {
    'categories': categories,
    'books': books
  })