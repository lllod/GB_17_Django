from django.contrib import admin
from .models import Client, Order, Product


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'client_registration_date', 'phone_number', 'client_address']
    list_filter = ['client_registration_date', 'name']
    search_fields = ['name', 'email', 'client_registration_date']
    list_editable = ['phone_number', 'email', 'client_address']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_description', 'product_price', 'product_date_added',
                    'product_image']
    list_filter = ['product_name', 'product_date_added', 'product_price']
    search_fields = ['product_name', 'product_date_added', 'product_description']
    list_editable = ['product_description', 'product_price', 'product_image']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_price', 'order_date']
    list_filter = ['order_date']
    search_fields = ['order_date']

