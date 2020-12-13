from django.http import HttpRequest
from seller_profile.models import Seller


def registerLoggedInSeller(request: HttpRequest) -> Seller:
    seller = Seller.objects.create(user=request.user.extension)
    request.user.extension.seller = seller

    return seller
