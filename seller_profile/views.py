from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from seller_profile.forms import ApartmentImageForm, RegisterApartment
from functions.getSeller import getSeller
from django.views import generic
from seller_profile.models import Apartment


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse("testing seller_profile")


@login_required
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

                return redirect(reverse('seller:apartment-list'))

    else:
        form = RegisterApartment()
        image = ApartmentImageForm()
    context['form'] = form
    context['image'] = image
    return render(request, 'seller/apartment-register.html', context)


@login_required
def updateApartment(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    context = dict()

    pk = request.GET.get('pk')
    apt = Apartment.objects.filter(pk=pk)[0]

    if apt.owner.user_extension.user.pk != request.user.pk:
        return render(request, 'seller/apartment-not-belong.html')

    aptImg = apt.images.first()

    if request.method == 'POST':
        form = RegisterApartment(request.POST, instance=apt)
        image = ApartmentImageForm(request.POST, request.FILES,
                                   instance=aptImg)  # passing only FILES does not work

        if form.is_valid():
            form.save()

            messages.success(request,
                             f"apartment @ {apt} updated")

            if image.is_valid():
                img = image.save()
                messages.success(request,
                                 f"image saved {img}")

                return redirect(reverse("seller:apartment-detail", kwargs={"pk": pk}))

    else:
        form = RegisterApartment(instance=apt)
        image = ApartmentImageForm(instance=aptImg)
    context['form'] = form
    context['image'] = image
    return render(request, 'seller/apartment-register.html', context)


class ApartmentList(generic.ListView):
    template_name = 'seller/apartment-list.html'
    queryset = Apartment.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        get = self.request.GET

        if not get:
            return qs

        if 'pk' in get.keys():
            if pk := get.get('pk'):
                qs = qs.filter(owner__pk=pk)
            else:
                qs = []

        return qs


class ApartmentDetail(generic.DetailView):
    template_name = 'seller/apartment-detail.html'
    queryset = Apartment.objects.all()



