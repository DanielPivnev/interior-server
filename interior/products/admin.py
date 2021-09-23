from django.contrib import admin
from products.models import ProductsCategory, Product, ProductsSlidersImages, Contacts

# Register your models here.

admin.site.register(ProductsCategory)
admin.site.register(Product)
admin.site.register(ProductsSlidersImages)
admin.site.register(Contacts)
