from django.db import models


# Create your models here.


class ProductsCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    action = models.BooleanField(default=False, null=True)
    descriptions = models.TextField(max_length=1000, blank=False, null=False)
    hover_icon_description = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.category} | {self.title}'
