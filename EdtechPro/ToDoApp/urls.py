from django.urls import path
from . import views

urlpatterns = [
    path('add-category/',views.CategoryCreateView.as_view(),name='add_category'),
    path('add-task/',views.TaskCreateView.as_view(),name='add_task'),
    path('show-category/',views.CategoryListView.as_view(),name='show_category'),
    path('show-task/',views.TaskListView.as_view(),name='show_task'),
    path('update-category/<int:pk>/',views.CategoryUpdateView.as_view(),name='update_category'),
    path('update-task/<int:pk>/',views.TaskUpdateView.as_view(),name='update_task'),
    path('delete-category/<int:pk>/',views.CategoryDeleteView.as_view(),name='delete_category'),
    path('delete-task/<int:pk>/',views.TaskDeleteView.as_view(),name='delete_task'),
]