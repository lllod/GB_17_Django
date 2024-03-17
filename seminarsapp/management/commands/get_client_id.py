from django.core.management.base import BaseCommand
from seminarsapp.models import Client


class Command(BaseCommand):
    help = 'Get client by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('id')
        client = Client.objects.get(id=client_id)
        self.stdout.write(f'{client}')
        # return client
