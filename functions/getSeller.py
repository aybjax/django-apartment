from django.http import HttpRequest
from functions.registerLoggedInSeller import registerLoggedInSeller


def getSeller(request: HttpRequest):
    justRegistered = True
    try:
        seller = request.user.user_extension.seller
    except:
        seller = registerLoggedInSeller(request)
    else:
        justRegistered = False

    return seller, justRegistered
