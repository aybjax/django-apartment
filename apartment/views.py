from django.http import HttpRequest
from django.shortcuts import render, HttpResponse


def test(request: HttpRequest, *args, **kwargs) -> HttpResponse:
    return HttpResponse("<p>Testing apartments</p>")
