import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.views import generic
from functions.async_services import sendAsyncEmail, sendQueue_async
from functions.sendEmail import sendEmail
from seller_profile.forms import ComplaintForm
from seller_profile.models import Apartment
from .models import Extension
from . import forms
from functions.loginUser import loginUser
from functions.sendSqs import sendQueue, COMPLAINT_NAME, COMPLAINT_ATTR


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

            try:
                ...
                # sendEmail(request, messages)
                sendAsyncEmail(request, messages)
            except Exception as e:
                messages.error(request, e)

            # return redirect('seller:register-apartment')
            # return reverse('seller:register-apartment') - method POST and POST data are saved
            return redirect(reverse('profile-detail', kwargs={'pk':request.user.user_extension.pk}))
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
        userForm = forms.UserUpdateFLI(request.POST, instance=request.user)
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
        print(userForm)

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

            return redirect(reverse('update-personal'))
    else:
        form = forms.UserUpdateUsernameForm(instance=request.user)

    context['form'] = form

    return render(request, 'user/update_profile.html', context)


class ViewPersonalDetail(LoginRequiredMixin, generic.DetailView):
    queryset = Extension.objects.all()


@login_required
def complaint(request: HttpRequest, *args, **kwargs):
    context = dict()

    print(request.POST)

    if 'redirecting' in request.POST:
        form = ComplaintForm()

        complainTarget = dict()

        if userId := request.POST.get('owner-user-id', False):
            complainTarget['complainee-id'] = userId
            complainTarget['complainee'] = User.objects.get(pk=userId).get_full_name()

        if apartmentId := request.POST.get('apartment-id', False):
            complainTarget['complainee-apartment-id'] = apartmentId
            complainTarget['complainee-apartment'] = str(
                    Apartment.objects.get(pk=apartmentId)
            )

        request.session['complaint-target'] = json.dumps(complainTarget)

    elif request.method == 'POST':
        form = ComplaintForm(request.POST)

        if form.is_valid():
            msgBody = dict()

            jsonTarget = request.session.get('complaint-target')
            dictTarget = json.loads(jsonTarget)

            for key, val in dictTarget.items():
                msgBody[key] = val

            msgBody['complainant'] = request.user.username
            msgBody['about'] = form.cleaned_data['type']
            msgBody['title'] = form.cleaned_data['title']
            msgBody['description'] = form.cleaned_data['description']

            jsonMsg = json.dumps(msgBody)

            messages.success(request, f'msg => {jsonMsg}')

            form = ComplaintForm()

            del request.session['complaint-target']

            # queueId = sendQueue(jsonMsg, COMPLAINT_NAME, COMPLAINT_ATTR)
            # sendQueue_async(jsonMsg, COMPLAINT_NAME, COMPLAINT_ATTR)  # uncomment
    else:
        form = ComplaintForm()

    context['form'] = form

    return render(request, 'complaint/complaint.html', context)
