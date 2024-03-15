from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(unique=True, null=False, blank=False, region='RU')
    client_address = models.CharField(max_length=500)
    client_registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'Name: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nAddress: {self.client_address}\n'
            f'Registration Date: {self.client_registration_date}')


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
    product_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Product Name: {self.product_name}\nProduct Description: {self.product_description}\n'
                f'Product Price: ${self.product_price}\nProduct Count: {self.product_count}')


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name, self.product.name
