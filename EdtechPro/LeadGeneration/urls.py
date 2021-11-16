from django.urls import path
from . import views

urlpatterns = [
    path('generate/',views.generateLeadView,name='generate_lead'),
]