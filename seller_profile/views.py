from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from seller_profile.forms import RegisterApartment
from seller_profile.functions.getSeller import getSeller
from seller_profile.models import Seller
from django.core.files.temp import gettempdir


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse("testing seller_profile")


# @login_required
def registerApartment(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    context = dict()
    if request.method == 'POST':
        form = RegisterApartment(request.POST)
        # if request.POST.get('add-another-apartment') == 'add':
        #     print(request.session.keys())
        #     if "numPhoto" in request.session.keys():
        #         request.session['numPhoto'] += 1
        #     else:
        #         request.session['numPhoto'] = 1
        #     # print(request.session['numPhoto'])
        #     # print(
        #     #         dir(request.FILES.get("photo"))
        #     # )
        #     # print(request.FILES.get("photo").size)
        #     # # request.session['files'] = request.FILES
        #     # filenames = [filename for filename in request.FILES['photo']]
        #     # # request.session['files'] = filenames
        #     # print(filenames)
        #     tmp_dir = gettempdir()
        #     import os; os.listdir(tmp_dir)
        #     print(os.listdir('/tmp'))
        #     print("*"*50)
        for photo in request.FILES:
            ...
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.owner, justRegistered = getSeller(request)
            if justRegistered:
                messages.success(
                        request,
                        "%s, congratulations with registering the first apartment" % (
                                request.user.username
                        )
                )
            apartment.save()
            messages.success(request,
                             f"apartment @ {apartment} saved")
            # return redirect(reverse('seller:test'))
    else:
        form = RegisterApartment()
    context['form'] = form
    return render(request, 'seller/register.html', context)
