from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

class UserRegistrationForm(UserCreationForm):
  phone_no = forms.CharField(max_length = 11)
  city = forms.CharField(max_length = 50)
  street = forms.CharField(max_length = 50)
  postal_code = forms.CharField(max_length = 50)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ,'phone_no', 'city', 'street', 'postal_code']

  def save(self, commit = True):
    user = super().save(commit = False)

    if commit == True:
      user.save()

      phone_no = self.cleaned_data['phone_no']
      city = self.cleaned_data['city']
      street = self.cleaned_data['street']
      postal_code = self.cleaned_data['postal_code']

      UserAccount.objects.create(
        user = user,
        account_id = 11111+user.id,
        phone_no = phone_no,
        city = city,
        street = street,
        postal_code = postal_code
      )

      return user

class UserProfileForm(forms.ModelForm):
  phone_no = forms.CharField(max_length = 11)
  city = forms.CharField(max_length = 50)
  street = forms.CharField(max_length = 50)
  postal_code = forms.CharField(max_length = 50)

  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone_no', 'city', 'street', 'postal_code']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    if self.instance:
      try:
        user = self.instance
        user_account = self.instance.account
      except UserAccount.DoesNotExist:
        user = None
        user_account = None

      if user_account:
        self.fields['phone_no'].initial = user_account.phone_no
        self.fields['city'].initial = user_account.city
        self.fields['street'].initial = user_account.street
        self.fields['postal_code'].initial = user_account.postal_code

  def save(self, commit = True):
    user = super().save(commit = False)

    if commit == True:
      user.save()

      user_account, created = UserAccount.objects.get_or_create(user = user)

      user_account.phone_no = self.cleaned_data['phone_no']
      user_account.city = self.cleaned_data['city']
      user_account.street = self.cleaned_data['street']
      user_account.postal_code = self.cleaned_data['postal_code']

      user_account.save()

      return user
    
class UserDeositForm(forms.ModelForm):
  class Meta:
    model = UserAccount
    fields = ['balance']