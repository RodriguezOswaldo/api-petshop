from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
# Create your models here.

class Client(User):
    phone = models.CharField(
        max_length=11
    )
    address_1 = models.CharField(
        max_length=30
    )
    address_2 = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Category(models.Model):
    name = models.CharField(
        max_length=15
    )
    color = ColorField(
        default='#FF0000'
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ProductCategory(Category):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Products Categories'


class PetCategory(Category):
    class Meta:
        verbose_name = 'Pet Category'
        verbose_name_plural = 'Pets Categories'

#Clase abstracta que trae los atributos para products y Pet
class Item(models.Model):
    name = models.CharField(
        max_length=20
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    description = models.TextField()
    photo = models.ImageField(
        upload_to='Photos'
    )
    stock = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        abstract = True


class Pet(Item):
    category = models.ForeignKey(
        PetCategory,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'


class Product(Item):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    shipped = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name ='Order'
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    quantity = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'



