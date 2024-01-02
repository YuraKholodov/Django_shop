from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context=context)


def about(request: HttpRequest):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о магазине, и почему надо покупать товары только в нем",
    }
    return render(request, "main/about.html", context=context)
