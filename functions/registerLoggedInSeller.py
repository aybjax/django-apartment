from django.http import HttpRequest
from seller_profile.models import Seller


def registerLoggedInSeller(request: HttpRequest) -> Seller:
    seller = Seller.objects.create(user_extension=request.user.user_extension)
    request.user.user_extension.seller = seller

    return seller
