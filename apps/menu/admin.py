# Django
from django.contrib import admin

# Local
from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = (
        "menu", "title", "url", "named_url", "parent"
    )
    list_filter = (
        "menu", "title", "url", "named_url", "parent"
    )
    search_fields = (
        "menu", "title", "url", "named_url", "parent"
    )
