from django.http import HttpRequest
from seller_profile.functions.registerLoggedInSeller import registerLoggedInSeller


def getSeller(request: HttpRequest):
    justRegistered = True
    try:
        seller = request.user.extension.seller
    except:
        seller = registerLoggedInSeller(request)
    else:
        justRegistered = False

    return seller, justRegistered
