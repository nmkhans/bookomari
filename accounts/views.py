from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
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