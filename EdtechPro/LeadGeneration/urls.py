from django.urls import path
from . import views

urlpatterns = [
    path('generate/',views.generateLeadView,name='generate_lead'),
    path('update/<int:leadid>/',views.updateLeadView,name='update_lead'),
    path('show/',views.showLeadsView,name='show_leads'),
]