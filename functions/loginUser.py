from django.contrib.auth import authenticate, login
from django.http import HttpRequest


def loginUser(request: HttpRequest) -> bool:
    username = request.POST.get("username")
    password = request.POST.get("password1")
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return True

    return False
