from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, get_list_or_404

from goods.models import Products


def catalog(request: HttpRequest, category_slug: str):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

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
