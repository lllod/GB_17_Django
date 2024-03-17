from django.core.management.base import BaseCommand
from seminarsapp.models import Client
from faker import Faker
from datetime import datetime


class Command(BaseCommand):
    help = 'Create fake clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of fake clients')

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')
        count = kwargs['count']
        for i in range(count):
            name = fake.first_name()
            email = fake.unique.email()
            phone_number = fake.phone_number()
            client_address = fake.address()
            client_registration_date = datetime.strptime(fake.date(), '%Y-%m-%d')
            client = Client(name=name, email=email, phone_number=phone_number, client_address=client_address,
                            client_registration_date=client_registration_date)
            client.save()
            self.stdout.write(f'Client {name} | {email} | {phone_number} was added to database')
