from django.core.management.base import BaseCommand
from seminarsapp.models import Client


class Command(BaseCommand):
    help = 'Update client name by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client id')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('id')
        client_name = kwargs.get('name')
        client = Client.objects.filter(id=client_id).first()
        client.name = client_name
        client.save()
        self.stdout.write(f'Udpate client:\n{client}')
        # return client
