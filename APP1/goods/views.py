from django.http import HttpRequest
from django.shortcuts import render

from goods.models import Products


def catalog(request: HttpRequest):
    goods = Products.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest, product_slug: str):
    prod = Products.objects.get(slug=product_slug)
    context = {'product': prod}
    return render(request, "goods/product.html", context=context)
