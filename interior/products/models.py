from django.db import models


# Create your models here.


class ProductsCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    main_image = models.ImageField(upload_to='products_images', blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    action = models.BooleanField(default=False, null=True)
    descriptions = models.JSONField(default=list, blank=False, null=False)
    hover_icon_description = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.category} | {self.title}'


class ProductsSlidersImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='id')
    image = models.ImageField(upload_to='products_sliders_images', blank=True)

    def __str__(self):
        return f'{self.product}'


class Contacts(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.city} | {self.address}'
