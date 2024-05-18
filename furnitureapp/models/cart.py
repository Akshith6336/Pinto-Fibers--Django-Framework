from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .product import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="", null=True, blank=True)
    product_qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
