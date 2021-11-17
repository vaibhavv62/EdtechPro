from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registerView,name='register'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('forgot-password/',views.forgotPasswordView,name='forgotpw'),
]