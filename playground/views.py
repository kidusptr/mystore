from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, ExpressionWrapper, F, DecimalField
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    try:
        discounted_price = ExpressionWrapper(
            F("unit_price") * 0.8, output_field=DecimalField()
        )
        queryset = Product.objects.annotate(discount_price=discounted_price)

    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "result": list(queryset)})


# Create your views here.
