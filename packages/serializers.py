from rest_framework import serializers

from packages.models import Package
from products.models import Product
from products.serializers import ProductSerializer
from boxes.models import Box
from boxes.serializers import BoxSerializer


class PackageSerializer(serializers.ModelSerializer):

    box_id = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    box = BoxSerializer(
        read_only=True,
    )

    product_id = serializers.ModelField(
        model_field=Package._meta.get_field('product_id')
    )

    product = ProductSerializer(
        read_only=True,
    )

    class Meta:

        model = Package

        fields = (
            'id',
            'box_id',
            'box',
            'product_id',
            'product',
        )
