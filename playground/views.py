from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product


def say_hello(request):
    try:
        queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "products": list(queryset)})


# Create your views here.
