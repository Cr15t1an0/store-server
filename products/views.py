from django.shortcuts import render
from products.models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)

def products(requests):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),

    }
    return render(requests, 'products/products.html', context)

