from django.core.management.base import BaseCommand
from seminar2app.models import Product


class Command(BaseCommand):
    help = 'Delete product by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Product id')

    def handle(self, *args, **kwargs):
        product_id = kwargs.get('id')
        product = Product.objects.filter(id=product_id).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'Product ID: {product_id} deleted')
        # return product
