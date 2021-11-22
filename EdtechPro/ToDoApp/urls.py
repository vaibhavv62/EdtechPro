from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.CategoryCreateView.as_view(),name='add_category'),
    path('show/',views.CategoryListView.as_view(),name='show_category'),
    path('update/',views.CategoryUpdateView.as_view(),name='update_category'),
    path('delete/',views.CategoryDeleteView.as_view(),name='delete_category'),
]