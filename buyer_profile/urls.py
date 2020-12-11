from django.urls import path
from . import views


app_name = 'buyer_profile'
urlpatterns = [
    path('test/', views.test, name='test'),
]
