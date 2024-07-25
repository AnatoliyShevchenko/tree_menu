# Django
from django.contrib import admin

# Local
from .models import Menu, MenuItem, Category


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ("title",)
    
    

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ("menu", "title", "category")
    list_filter = ("menu", "title", "category")
    search_fields = ("menu", "title", "category")
