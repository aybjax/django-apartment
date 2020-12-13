from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . import forms


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse('<h1>Test from User_extended</h1>')


def registerUser(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    context = dict()

    if request.method == 'POST':
        userForm = forms.UserForm(request.POST)
        extensionForm = forms.UserExtendedForm(request.POST, request.FILES)

        if all([
                userForm.is_valid(), extensionForm.is_valid(),
        ]):
            user = userForm.save()
            extension = extensionForm.save(commit=False)
            extension.user = user

            extension.save()

            successMessage = "Account %s is successfully created" % user.username

            messages.success(request, successMessage)
            loginUser(request)

            return redirect('seller:register-apartment')
            # return reverse('seller:register-apartment') - method POST and POST data are saved

        else:
            messages.error(request, "form not valid")

            if not userForm.is_valid():
                messages.error(request, "user form not valid")
                messages.error(request, userForm)

            if not extensionForm.is_valid():
                messages.error(request, "extension form not valid")
                messages.error(request, extensionForm)

    else:
        userForm = forms.UserForm()
        extensionForm = forms.UserExtendedForm()

    context['form'] = userForm
    context['formExtension'] = extensionForm

    return render(request, 'user/register.html', context)


def loginUser(request: HttpRequest):
    username = request.POST.get("username")
    password = request.POST.get("password1")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
