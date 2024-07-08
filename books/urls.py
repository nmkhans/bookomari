from django.urls import path
from . import views

urlpatterns = [
  path('add/', views.AddBookView.as_view(), name = 'add-book'),
  path('detail/<slug:book_slug>/', views.book_detail, name = 'book-detail'),
]
