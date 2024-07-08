from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'account')
  account_id = models.CharField(max_length=50)
  balance = models.DecimalField(default = 0, decimal_places = 2, max_digits = 12)
  phone_no = models.CharField(max_length = 11)
  city = models.CharField(max_length = 50)
  street = models.CharField(max_length = 50)
  postal_code = models.CharField(max_length = 50)
  created_at = models.DateField(auto_now_add = True)

  def __str__(self):
    return f"user {self.user.username}"