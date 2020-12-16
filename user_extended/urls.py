from django.urls import path
from django.contrib.auth import views as auth_views
from user_extended import views
from django.contrib.auth import views as auth_views

# app cannot be used unless password reset app names cannot resolve
urlpatterns = [
        path('test/', views.test, name='test'),
        path('register/', views.registerUser, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),
             name='logout'),
        path('update-personal/', views.updatePersonal, name="update-personal"),
        path('update-username/', views.updateUsername, name="update-username"),
        path('personal-detail/<int:pk>',
             views.ViewPersonalDetail.as_view(template_name='user/detail_profile.html'),
             name="profile-detail"),

        ##################
        # password stuff #
        ##################
        path('password-reset/',
             auth_views.PasswordResetView.as_view(template_name='password/password-reset.html'),
             name='password_reset'),
        path('password-reset/done/',
             auth_views.PasswordResetDoneView.as_view(
                     template_name='password/password-reset-done.html'),
             name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/',
             auth_views.PasswordResetConfirmView.as_view(
                     template_name='password/password-reset-confirm.html'),
             name='password_reset_confirm'),
        path('password-reset-complete/',
             auth_views.PasswordResetCompleteView.as_view(
                     template_name='password/password-reset-complete.html'),
             name='password_reset_complete'),
]
