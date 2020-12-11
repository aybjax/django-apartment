from django.urls import path
from django.contrib.auth import views as auth_views
from user_extended import views

app_name = 'user_extended'
urlpatterns = [
        path('test/', views.test, name='test'),
        path('register/', views.registerUser, name='register'),
]
