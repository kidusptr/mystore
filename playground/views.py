from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
    try:
        queryset = Product.objects.defer("description")

    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "products": list(queryset)})


# Create your views here.
