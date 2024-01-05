from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, get_list_or_404

from goods.models import Products


def catalog(request: HttpRequest, category_slug: str):
    page = request.GET.get('page', 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request: HttpRequest, product_slug: str):
    prod = Products.objects.get(slug=product_slug)
    context = {'product': prod}
    return render(request, "goods/product.html", context=context)
