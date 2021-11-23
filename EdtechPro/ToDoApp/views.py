from django.shortcuts import render

from .forms import TaskModelForm
from .models import Category,Task
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    fields = '__all__'
    success_url = '/to-do/show-category/'
    # template_name = 'ToDoApp/category_form.html'

class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    # template_name = 'ToDoApp/category_list.html'

class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/to-do/show-category/'

class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    success_url = '/to-do/show-category/'
    # template_name = 'ToDoApp/category_confirm_delete.html'

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    def get_queryset(self):
        user = self.request.user
        object_list = Task.objects.filter(task_for=user)
        return object_list

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskModelForm
    success_url = '/to-do/show-task/'
    def get_initial(self):
        return {'task_for':self.request.user}

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskModelForm
    success_url = '/to-do/show-task/'

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/to-do/show-task/'

