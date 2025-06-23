from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    try:
        queryset = Product.objects.order_by("title")
        products = Product.objects.order_by("unit_price", "-title")
        product = Product.objects.earliest("unit_price")
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "product": product})


# Create your views here.
