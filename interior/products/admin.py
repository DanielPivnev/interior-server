from django.contrib import admin
from products.models import ProductsCategory, Product, ProductsSlidersImage, Contact

# Register your models here.

admin.site.register(ProductsCategory)
admin.site.register(Product)
admin.site.register(ProductsSlidersImage)
admin.site.register(Contact)
