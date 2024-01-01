from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse("Home page")


def about(request: HttpRequest):
    return HttpResponse("About page")
