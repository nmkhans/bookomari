from django.urls import path
from . import views

urlpatterns = [
  path('add/', views.AddBookView.as_view(), name = 'add-book')
]
