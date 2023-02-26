"""Views.py (Product App)"""
from django import apps
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . models import Product, ProductFilter
from django.template import loader


# Create your views here.

def index(request):
    """Index"""
    f = ProductFilter(
        request.GET, queryset=Product.objects.all().order_by('code'))
    has_filter = any(field in request.GET for field in set(f.get_fields()))

    return render(request, 'products/index.html', {
        'filter': f,
        'has_filter': has_filter
    })


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


# def index(request):
#     """Index"""
#     products = Product.objects.all()
#     return render(request, 'products/index.html', {'products': products})


# def showlist(request):
#         results = Product.objects.all
#         return render(request, "products/results.html", {"showproduct": results})


# def results(request):
#     # | Product.objects.filter(firstname='Tobias').values()
#     mydata = Product.objects.filter(name__startswith='C').values()
#     template = loader.get_template('products/results.html')
#     context = {
#         'products': mydata,
#     }
#     return HttpResponse(template.render(context, request))
    # products = Product.objects.all
    # return render(request, "products/results2.html", {'products': products})

# def search(request):
#     product_list = Product.objects.all()
#     product_filter = ProductFilter(request.GET, queryset=product_list)
#     return render(request, 'products/search/product_list.html', {'filter': product_filter})


# def results(request):
#     product_list = Product.objects.all()
#     product_filter = ProductFilter(request.GET, queryset=product_list)
#     return render(request, 'products/results.html', {'filter': product_filter})


# def results(request):
#     f = ProductFilter(
#         request.GET, queryset=Product.objects.all().order_by('code'))
#     has_filter = any(field in request.GET for field in set(f.get_fields()))

#     return render(request, 'products/results.html', {
#         'filter': f,
#         'has_filter': has_filter
#     })
