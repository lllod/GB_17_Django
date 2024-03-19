from django.core.management.base import BaseCommand
from seminarsapp.models import Client, Order, Product, OrderProduct
from django.db.models import F, Sum
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Update client name by id'

    # def add_arguments(self, parser):
    #     parser.add_argument('id', type=int, help='Client id')
    #     parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        date = timezone.now() - timedelta(days=7)
        self.stdout.write(f'{date}')
        p = OrderProduct.objects.filter(order__order_date__gte=date, order__customer=1)
        self.stdout.write(f'{[l.product_id for l in p]}')
        # pr = Product.objects.filter(orderproduct__order__customer=1, order__order_date__gte=date)
        pr = OrderProduct.objects.prefetch_related('order', 'product').filter(order__order_date__gte=date,
                                                                              order__customer=1).values(
            product_name=F('product__product_name'), product_price=F('product__product_price'))
        # self.stdout.write(f'{[(i.id, i.product_id)  for i in pr]}')
        self.stdout.write(f'{pr}')
        # for i in p:
        #     self.stdout.write(f'{Product.objects.get(pk=i.product_id).product_name}')
