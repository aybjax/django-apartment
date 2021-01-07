from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from PIL import Image

from .models import Extension


class EmailNotEmptyMixin:
    def clean_email(self):
        email = self.cleaned_data.get('email', 0)

        if email == 0:
            raise ValidationError("Email required")  # not needed

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")

        return email


class NamesNotEmptyMixin:
    def clean_first_name(self):
        name = self.cleaned_data.get('first_name', "")

        if name == "":
            raise ValidationError("First name required")

        return name

    def clean_last_name(self):
        name = self.cleaned_data.get('last_name', "")

        if name == "":
            raise ValidationError("Last name required")

        return name


class UserForm(UserCreationForm, EmailNotEmptyMixin, NamesNotEmptyMixin):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
                'first_name', 'last_name', 'username',
                'email', 'password1', 'password2',
        ]

    # def clean(self):
    #     form_data = self.cleaned_data
    #     if form_data['password'] != form_data['password_repeat']:
    #         self._errors["password"] = ["Password do not match"]  # Will raise a error message
    #         del form_data['password']
    #     return form_data


class UserExtendedForm(forms.ModelForm):
    class Meta:
        model = Extension
        fields = [
                'city', 'image'
        ]
        # exclude = ["user"] # this version does not save image


class UserUpdateFLI(forms.ModelForm, NamesNotEmptyMixin):
    class Meta:
        model = User
        fields = [
                'first_name', 'last_name'
        ]
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': 'inline-block w-full hover:bg-purple-900 hover:text-gray-200 p-2'})
            self.fields['last_name'].widget.attrs.update({'class': 'inline-block w-full hover:bg-purple-900 hover:text-gray-200 p-2'})


class UserExtendedUpdateFLI(forms.ModelForm):
    class Meta:
        model = Extension
        fields = [
                'city',
                'image',
        ]
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city'].widget.attrs.update({'class': 'inline-block w-full hover:bg-purple-900 hover:text-gray-200 p-2'})
            self.fields['image'].widget.attrs.update({'class': 'inline-block w-full hover:bg-purple-900 hover:text-gray-200 p-2'})


class UserUpdateUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                'username', 'email'
        ]
