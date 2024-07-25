# Django
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("id",)
        verbose_name = "меню"
        verbose_name_plural = "меню"

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ("id",)
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    menu = models.ForeignKey(
        Menu, related_name='items', on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category, related_name='categories', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "блюдо"
        verbose_name_plural = "блюда"

    def __str__(self):
        return self.title
    