from django.shortcuts import redirect
from django.urls import path, re_path, reverse
from . import views


app_name = 'seller'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('register-apartment/', views.registerApartment, name='register-apartment'),
    path('apartments/<int:pk>/', views.ApartmentDetail.as_view(), name='apartment-detail'),
    path('update-apartment/', views.updateApartment, name='update-apartment'),
    path('apartments/', views.ApartmentList.as_view(), name='apartment-list'),
    # re_path(r'[\w\d?=]*', lambda *args, **kwargs: redirect(reverse('seller:apartment-list')),
    #         name='catch-all'),
]
