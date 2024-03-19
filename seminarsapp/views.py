import logging

from django.shortcuts import render
from django.db.models import F
from django.core.files.storage import FileSystemStorage
from .models import Client, OrderProduct, Product
from .forms import AddProductForm, AddImage
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


def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_description = form.cleaned_data['product_description']
            product_price = form.cleaned_data['product_price']
            product_count = form.cleaned_data['product_count']
            product_date_added = form.cleaned_data['product_date_added']
            product_image = form.cleaned_data['product_image']
            logger.info('Получены данные о новом продукте')
            file_save = FileSystemStorage()
            file_save.save(product_image.name, product_image)
            new_product = Product(product_name=product_name, product_description=product_description,
                                  product_price=product_price, product_count=product_count,
                                  product_date_added=product_date_added, product_image=product_image)
            new_product.save()
            logger.info('Данные о новом продукты сохранены')
    else:
        form = AddProductForm()
    context = {
        'title': 'Add Product',
        'form': form,
    }
    return render(request, 'seminarsapp/product-add.html', context)


def img_add(request):
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            file_save = FileSystemStorage()
            file_save.save(image.name, image)
    else:
        form = AddImage()
    context = {
        'title': 'Add Product',
        'form': form,
    }
    return render(request, 'seminarsapp/img-add.html', context)
