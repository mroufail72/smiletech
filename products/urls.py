"""Products URLs"""
from django.urls import path, re_path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    #  path('results.html', views.showlist, name='showlist'),
    path('<int:product_id>', views.detail, name='detail'),
    # path('results.html', views.results, name='index'),
    # re_path(r'^search/$', views.search, name='search'),
    # path('results.html', views.results, name='results'),
]
