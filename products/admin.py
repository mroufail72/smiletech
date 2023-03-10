from django.contrib import admin
from . models import Type, Product


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'type', 'name', 'description')
    exclude = ('date_created', 'selected_yn')


admin.site.register(Type, TypeAdmin)
admin.site.register(Product, ProductAdmin)
