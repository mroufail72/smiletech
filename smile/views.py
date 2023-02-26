from django.shortcuts import render
from products.models import Product
from products.models import ProductList


def home(request):
    return render(request, 'home.html')


def showlist(request):
    results = Product.objects.all
    return render(request, "home.html", {"showproduct": results})
