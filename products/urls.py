from django.urls import path
from products.views import products

app_name = 'products'

urllpaterns = [
    path('', products, name='index'),
]