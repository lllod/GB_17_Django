from django.core.management.base import BaseCommand
from seminarsapp.models import Order, OrderProduct, Product, Client
from faker import Faker
from datetime import datetime
from random import randint


class Command(BaseCommand):
    help = 'Create fake orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of fake orders')

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        count = kwargs['count']
        for i in range(count):
            customer = Client.objects.get(id=randint(Client.objects.first().id, Client.objects.last().id))
            order_price = 0
            order_date = datetime.strptime(fake.date(), '%Y-%m-%d')
            order = Order(customer=customer, order_price=order_price, order_date=order_date)
            order.save()
            self.stdout.write(f'Order {i + 1} was added to database')

        for order in Order.objects.all():
            for i in range(randint(1, 5)):
                order_product = OrderProduct(
                    order=Order.objects.get(id=order.id),
                    product=Product.objects.get(id=randint(Product.objects.first().id,
                                                           Product.objects.last().id)))
                order_product.save()

        for order in Order.objects.all():
            orders_per_id = OrderProduct.objects.filter(order_id=order.id)
            order_total_sum = 0
            for i in range(orders_per_id.count()):
                order_total_sum += Product.objects.get(id=orders_per_id[i].product_id).product_price
            upd_order = order
            upd_order.order_price = order_total_sum
            upd_order.save()


