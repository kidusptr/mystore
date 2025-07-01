from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Product
        fields = ["id", "title", "unit_price"]
