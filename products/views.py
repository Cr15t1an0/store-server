from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def products(requests):
    return render(requests, 'products/products.html')

def test_context(requests):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ]

    }
    return render(requests, 'products/test-context.html', context)