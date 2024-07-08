from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CategoryForm
from django.contrib import messages
from django.template.defaultfilters import slugify

# Create your views here.
class AddCategoryView(CreateView):
  template_name = 'categories/add_category.html'
  form_class = CategoryForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    category = form.save(commit = False)
    category.slug = slugify(category.name)
    category.save()
    
    messages.success(self.request, 'Category added')
    return super().form_valid(form)