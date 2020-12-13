from django import forms
from .models import Apartment, ApartmentImage


class RegisterApartment(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ['owner']


class ApartmentImageForm(forms.ModelForm):
    class Meta:
        model = ApartmentImage
        fields = ['image']
