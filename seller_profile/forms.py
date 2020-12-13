from django import forms
from .models import Apartment


class RegisterApartment(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ['owner']


# class ApartmentImageForm(forms.Form):

