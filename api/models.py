from django.db import models
import tastypie.resources
import products.models
import tastypie.fields


class TypeResource(tastypie.resources.ModelResource):
    class Meta:
        queryset = products.models.Type.objects.all()
        resource_name = 'types'


class ProductResource(tastypie.resources.ModelResource):
    # type = fields.ForeignKey(TypeResource, 'type')
    # types = fields.ToManyField(TypeResource, 'type_set')
    # type = fields.ForeignKey(TypeResource, 'type')
    # type = fields.ToOneField(TypeResource, 'type', full=True)
    type = tastypie.fields.ForeignKey(
        TypeResource, attribute='type', null=True)

    class Meta:
        queryset = products.models.Product.objects.all()
        resource_name = 'products'
        excludes = ['date_created', 'selected_yn']
