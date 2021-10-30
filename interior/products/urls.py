from django.urls import path
from .views import products


app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:c_id>/<int:page>', products, name='category')
]
