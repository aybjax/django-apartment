from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from seller_profile.forms import ApartmentImageForm, RegisterApartment
from seller_profile.functions.getSeller import getSeller
from seller_profile.models import ApartmentImage


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse("testing seller_profile")


# @login_required
def registerApartment(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    context = dict()
    if request.method == 'POST':
        form = RegisterApartment(request.POST)
        image = ApartmentImageForm(request.POST, request.FILES)  # passing only FILES does not work

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

            if image.is_valid():
                img = image.save(commit=False)
                img.apartment = apartment
                img.save()
                messages.success(request,
                                 f"image saved {img}")
            else:
                messages.error(request, "image could not be saved")
            # for image in request.FILES:
            #     imageModel = ApartmentImage.objects.create(
            #             apartment=apartment, image=image
            #     )
            #     imageModel.save()

            # return redirect(reverse('seller:test'))
    else:
        form = RegisterApartment()
        image = ApartmentImageForm()
    context['form'] = form
    context['image'] = image
    return render(request, 'seller/register.html', context)
