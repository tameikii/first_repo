from functools import total_ordering
from django.db import models
from django.conf import settings
from mamazon.models import Product


User = settings.AUTH_USER_MODEL

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total =
    created
    updated
