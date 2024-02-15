from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_en")


@admin.register(Product)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title_ru', "title_ru")

