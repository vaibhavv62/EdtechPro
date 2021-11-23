from django.shortcuts import render

from .forms import TaskModelForm
from .models import Category,Task
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/to-do/show-category/'
    # template_name = 'ToDoApp/category_form.html'

class CategoryListView(ListView):
    model = Category
    # template_name = 'ToDoApp/category_list.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/to-do/show-category/'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/to-do/show-category/'
    # template_name = 'ToDoApp/category_confirm_delete.html'

class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    success_url = '/to-do/show-task/'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskModelForm
    success_url = '/to-do/show-task/'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/to-do/show-task/'

