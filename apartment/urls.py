from django.urls import path
from . import views


app_name = 'apartment'
urlpatterns = [
    path('test/', views.test, name='test')
]
