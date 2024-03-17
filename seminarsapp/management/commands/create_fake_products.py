from django.core.management.base import BaseCommand
from seminarsapp.models import Product
from faker import Faker
from datetime import datetime


class Command(BaseCommand):
    help = 'Create fake products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of fake products')

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        count = kwargs['count']
        for i in range(count):
            product_name = fake.text(max_nb_chars=100)
            product_description = fake.text(max_nb_chars=512)
            product_price = fake.pydecimal(min_value=0.1, max_value=100.0)
            product_count = fake.random_int(0, 100)
            product_date_added = datetime.strptime(fake.date(), '%Y-%m-%d')
            client = Product(product_name=product_name, product_description=product_description,
                             product_price=product_price, product_count=product_count,
                             product_date_added=product_date_added)
            client.save()
            self.stdout.write(f'Product {product_name} was added to database')
