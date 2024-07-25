# Django
from django.urls import path

# Local
from .views import get_menu


urlpatterns = [
    path("", get_menu),
    path("<str:menu_name>/", get_menu),
    path("<str:menu_name>/<str:category_name>/", get_menu),
    # path("<str:menu_name>/<str:category_name>/<str:item_name>/", get_menu),
]
