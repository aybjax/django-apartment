from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse("testing seller_profile")
