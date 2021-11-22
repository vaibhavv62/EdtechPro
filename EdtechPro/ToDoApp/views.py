from django.shortcuts import render
from .models import Category
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/to-do/show/'
    # template_name = 'ToDoApp/category_form.html'

class CategoryListView(ListView):
    model = Category
    # template_name = 'ToDoApp/category_list.html'

class CategoryUpdateView(UpdateView):
    model = Category

class CategoryDeleteView(DeleteView):
    pass


