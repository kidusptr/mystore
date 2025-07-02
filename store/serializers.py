from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name="collection-detail",
    )

    def calculate_tax(self, product):
        return product.unit_price + (product.unit_price * Decimal(0.15))

    class Meta:
        model = Product
        fields = ["id", "title", "price", "price_with_tax", "collection"]
