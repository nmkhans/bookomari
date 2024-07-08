from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import UserRegistrationForm, UserProfileForm, UserDeositForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib import messages

# Create your views here.
class UserRegisterView(FormView):
  template_name = 'accounts/user_register.html'
  form_class = UserRegistrationForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    messages.success(self.request, 'Account created.')
    return super().form_valid(form)

class UserLoginView(LoginView):
  template_name = 'accounts/user_login.html'

  def form_valid(self, form):
    messages.success(self.request, 'Login successfull.')
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse_lazy('home')
    
def user_logout(req):
  logout(req)
  messages.warning(req, 'Logout successfull.')
  return redirect('home')

class UserProfileView(View):
  template_name = 'accounts/user_profile.html'

  def get(self, req):
    form = UserProfileForm(instance = req.user)

    return render(req, 'accounts/user_profile.html', {
      'form': form
    })

  def post(self, req):
    form = UserProfileForm(req.POST, instance = req.user)

    if form.is_valid():
      form.save()
      messages.success(req, 'Profile updated.')
      return redirect('user-profile')

    return render(req, 'accounts/user_profile.html', {
      'form': form
    })
  
class UserPasswordChange(PasswordChangeView):
  template_name = 'accounts/user_password_change.html'
  model = User
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    messages.success(self.request, 'Password updated')
    return super().form_valid(form)
  
class UserDepositView(FormView):
  template_name = 'accounts/user_deposit.html'
  form_class = UserDeositForm
  model = UserAccount
  success_url = reverse_lazy('home')

  def get_initial(self):
    initial = {'balance': ''}
    return initial

  def form_valid(self, form):
    deposited_balance = form.cleaned_data['balance']
    user_account = self.request.user.account
    user_account.balance += deposited_balance
    user_account.save()  

    messages.success(self.request, f"Amount {deposited_balance} has been deposited into your balance")  

    return super().form_valid(form)