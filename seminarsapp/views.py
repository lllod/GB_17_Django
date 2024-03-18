import logging

from django.shortcuts import render
from django.db.models import F
from .models import Client, OrderProduct
from django.utils import timezone
from datetime import timedelta

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    all_clients = Client.objects.all()
    context = {
        'title': 'All clients',
        'h1': 'all clients list',
        'clients': all_clients,
    }
    print(all_clients)
    return render(request, 'seminarsapp/index.html', context)


def client_orders(request, client_id, days):
    logger.info('Client orders list page accessed')
    date = timezone.now() - timedelta(days=days)
    products = OrderProduct.objects.prefetch_related('order', 'product').filter(order__order_date__gte=date,
                                                                                order__customer=client_id).values(
        product_name=F('product__product_name'), product_price=F('product__product_price')).distinct()
    context = {
        'title': "Customer's orders",
        'h1': days,
        'products': products,
    }
    return render(request, 'seminarsapp/client-orders.html', context)


