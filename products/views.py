"""Views.py (Product App)"""
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . models import Product

# Create your views here.


def index(request):
    """Index"""
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})
