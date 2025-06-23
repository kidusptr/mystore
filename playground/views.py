from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    try:
        queryset = Product.objects.filter(title__icontains="coffee")
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "products": list(queryset)})


# Create your views here.
