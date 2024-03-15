from django.core.management.base import BaseCommand
from seminar2app.models import Product


class Command(BaseCommand):
    help = 'Get product by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Product id')

    def handle(self, *args, **kwargs):
        product_id = kwargs.get('id')
        product = Product.objects.get(id=product_id)
        self.stdout.write(f'{product}')
        # return product
