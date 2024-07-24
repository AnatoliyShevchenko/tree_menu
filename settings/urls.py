# Django
from django.contrib import admin
from django.urls import path, include

# Third-Party
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("menu.urls")),
] + debug_toolbar_urls()
