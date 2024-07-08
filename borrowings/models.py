from django.db import models
from accounts.models import UserAccount
from books.models import Book

BORROWING_STATUS = [
  ('borrowed', "Borrowed"),
  ('returned', "Returned"),
]

# Create your models here.
class Borrowing(models.Model):
  account = models.ForeignKey(UserAccount, on_delete = models.CASCADE, related_name = 'borrowings')
  book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'borrowings')
  borrowing_price = models.IntegerField()
  balance_after_borrowing = models.IntegerField()
  borrowing_date = models.DateField(auto_now_add = True)
  status = models.CharField(max_length = 100, choices=BORROWING_STATUS)

  class Meta:
    ordering = ['borrowing_date']

  def __str__(self):
    return f"Borrowing - {self.id}"