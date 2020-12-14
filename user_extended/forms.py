from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import Extension


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
                'first_name', 'last_name', 'username',
                'email', 'password1', 'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', 0)

        if email == 0:
            raise ValidationError("Email required")  # not needed

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        
        return email

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
