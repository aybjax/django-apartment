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


class ComplaintForm(forms.Form):
    choices = [
            ('seller', 'seller'),
            ('apartment', 'apartment'),
    ]

    type = forms.ChoiceField(choices=choices, label='Issue about')
    title = forms.CharField(max_length=20, label='Short description')
    description = forms.CharField(label='Describe complaint thoroughly', widget=forms.Textarea)
