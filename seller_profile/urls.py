from django.urls import path
from . import views


app_name = 'seller'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('register-apartment/', views.registerApartment, name='register-apartment'),
]
