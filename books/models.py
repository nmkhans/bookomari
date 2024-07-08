from django.db import models
from categories.models import Category

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length = 100)
  description = models.TextField()
  slug = models.SlugField(max_length = 100, null = True, blank = True)
  image = models.ImageField(upload_to="")
  borrowing_price = models.IntegerField()
  categories = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "books")

  def __str__(self):
    return f"book - {self.title}"