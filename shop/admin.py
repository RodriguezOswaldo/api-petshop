from django.contrib import admin
from .models import Client, ProductCategory, PetCategory, Product, Pet

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'get_full_name',
        'phone',
        'address_1',
        'address_2'
    ]


@admin.register(ProductCategory)
class ProductCategoryAdming(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'color'
    ]


@admin.register(PetCategory)
class PetCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'color'
    ]
    search_fields = [
        'name'
    ]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display =  [
        'id',
        'name',
        'price',
        'description',
        'photo',
        'stock',
        'category'
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'description',
        'photo',
        'stock',
        'category'
    ]

