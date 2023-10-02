from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# /products(url) -> index (function)

def index(request):
    products =  Product.objects.all()
    return render(request, 'index.html', {'products': products})
