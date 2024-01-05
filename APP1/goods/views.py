from django.http import HttpRequest
from django.shortcuts import render

from goods.models import Products


def catalog(request: HttpRequest, category_slug: str):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest, product_slug: str):
    prod = Products.objects.get(slug=product_slug)
    context = {'product': prod}
    return render(request, "goods/product.html", context=context)
