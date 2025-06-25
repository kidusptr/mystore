from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    try:
        queryset = Customer.objects.annotate(new_id=F("id") + 1)
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "result": list(queryset)})


# Create your views here.
