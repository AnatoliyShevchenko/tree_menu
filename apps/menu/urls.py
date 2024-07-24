# Django
from django.urls import path

# Local
from .views import get_menu


urlpatterns = [
    path("", get_menu),
]
