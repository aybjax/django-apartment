from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from . import forms
from .functions.loginUser import loginUser


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
            _ = loginUser(request)

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


@login_required
def updatePersonal(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    context = dict()

    if request.method == 'POST':
        userForm = forms.UserUpdateFLI(request.POST,
                                       instance=request.user)
        extensionForm = forms.UserExtendedUpdateFLI(request.POST, request.FILES,
                                                    instance=request.user.user_extension)

        if all([
                userForm.is_valid(), extensionForm.is_valid()
        ]):
            userForm.save()
            extensionForm.save()

            messages.success(request, "all valid")

        else:
            if not userForm.is_valid():
                messages.error(request, userForm.errors)
            if not extensionForm.is_valid():
                messages.error(request, extensionForm.errors)

    elif request.method == 'GET':
        userForm = forms.UserUpdateFLI(instance=request.user)
        extensionForm = forms.UserExtendedUpdateFLI(instance=request.user.user_extension)

    else:
        raise Http404

    context['form'] = userForm
    context['formExtension'] = extensionForm

    return render(request, 'user/update_profile_fli.html', context)


@login_required
def updateUsername(request: HttpRequest, *args, **kwargs):
    context = dict()

    if request.method == 'POST':
        form = forms.UserUpdateUsernameForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Username updated")

            return redirect(reverse('user:update-personal'))
    else:
        form = forms.UserUpdateUsernameForm(instance=request.user)

    context['form'] = form

    return render(request, 'user/update_profile.html', context)
