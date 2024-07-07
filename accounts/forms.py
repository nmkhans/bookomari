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

      if commit:
        user.save()

        phone_no = self.cleaned_data['phone_no']
        city = self.cleaned_data['city']
        street = self.cleaned_data['street']
        postal_code = self.cleaned_data['postal_code']

        UserAccount.objects.create(
          user = user,
          account_id = 00000+user.id,
          phone_no = phone_no,
          city = city,
          street = street,
          postal_code = postal_code
        )

        return user

