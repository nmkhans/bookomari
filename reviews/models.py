from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class Review(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'reviews')
  book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'reviews')
  content = models.TextField()
  created_at = models.DateField(auto_now_add = True)

  def __str__(self):
    return f"review by {self.user.username}"
