from django.urls import path
from . import views


app_name = 'seller_profile'
urlpatterns = [
    path('test/', views.test, name='test'),
]
