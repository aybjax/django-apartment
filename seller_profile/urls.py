from django.urls import path
from . import views


app_name = 'seller'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('register-apartment/', views.registerApartment, name='register-apartment'),
    path('apartments/', views.ApartmentList.as_view(), name='apartment-list'),
    path('apartments/<int:pk>/', views.ApartmentDetail.as_view(), name='apartment-detail'),
    path('update-apartment/', views.updateApartment, name='update-apartment'),
]
