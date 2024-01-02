from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    context = {"title": "Home", "content": "Главная страница магазина"}
    return render(request, "main/index.html", context=context)


def about(request: HttpRequest):
    return HttpResponse("About page")
