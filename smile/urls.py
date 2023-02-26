"""smile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import api.models
from . import views


product_resource = api.models.ProductResource()
type_resource = api.models.TypeResource()

urlpatterns = [
    # path('', views.home),
    path('', views.showlist, name='showlist'),
    path('base.html', views.showlist, name='showlist'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api/', include(product_resource.urls)),
    path('api/', include(type_resource.urls))
]

admin.site.site_header = "Smile! Lookup Admin"
admin.site.site_title = "Smile! Lookup Admin Portal"
admin.site.index_title = "Welcome to Smile! Lookup Portal"
