from django.urls import path
from .views import index, admin_users_delete, admin_users_update, admin_users_read, admin_users_create, \
    admin_users_deactivate, admin_users_activate, admin_products_read, admin_products_create


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users_read/', admin_users_read, name='admin_users_read'),
    path('users_create/', admin_users_create, name='admin_users_create'),
    path('users_update/<int:id>', admin_users_update, name='admin_users_update'),
    path('users_delete/<int:id>', admin_users_delete, name='admin_users_delete'),
    path('users_deactivate/<int:id>', admin_users_deactivate, name='admin_users_deactivate'),
    path('users_activate/<int:id>', admin_users_activate, name='admin_users_activate'),
    path('products_read/', admin_products_read, name='admin_products_read'),
    path('products_create/', admin_products_create, name='admin_products_create')
]
