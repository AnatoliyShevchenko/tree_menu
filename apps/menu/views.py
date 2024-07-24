# Django
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def get_menu(request: HttpRequest) -> HttpResponse:
    return render(
        request=request, template_name="index.html"
    )
