from rest_framework import fields, serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, 
        allow_empty_file=True, 
        allow_null=True,
        required=False
    )
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock',
            'is_active',
            'image',
            'category'
        )