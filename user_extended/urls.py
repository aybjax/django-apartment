from django.urls import path
from django.contrib.auth import views as auth_views
from user_extended import views
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
        path('', views.test, name='test'),
        path('register/', views.registerUser, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
             name='logout'),
        path('update-personal/', views.updatePersonal, name="update-personal"),
        path('update-username/', views.updateUsername, name="update-username"),
]
