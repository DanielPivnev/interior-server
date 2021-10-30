from django.db import models
from products.models import Product
from users.models import User


# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} | {self.product.title}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        return sum(basket.quantity * basket.product.price for basket in Basket.objects.filter(user=self.user))

    def total_quantity(self):
        return sum(basket.quantity for basket in Basket.objects.filter(user=self.user))