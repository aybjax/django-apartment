from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import forms


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse('<h1>Test from User_extended</h1>')


def registerUser(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    if request.method == 'POST':
        ...
    else:
        userForm = forms.UserForm()
        extensionForm = forms.UserExtendedForm()
    context = {
            'form': userForm,
            'formExtension': extensionForm,
    }

    return render(request, 'user/register.html', context)
