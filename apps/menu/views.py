# Django
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def get_menu(
    request: WSGIRequest, menu_name: str = None, 
    category_name: str = None
):
    context = {
        "menu_name": menu_name,
        "category_name": category_name,
    }
    return render(
        request=request, template_name="index.html", context=context
    )
