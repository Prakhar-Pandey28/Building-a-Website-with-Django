from django.http import HttpResponse
from django.shortcuts import render

# /products(url) -> index (function)

def index(request):
    return HttpResponse("Hello World")
