from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    try:
        queryset = Customer.objects.annotate(
            full_name=Func(
                F("first_name"), Value(" "), F("last_name"), function="CONCAT"
            )
        )

        test = Customer.objects.annotate(
            full_name=Concat("first_name", Value(" "), "last_name")
        )
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "result": list(test)})


# Create your views here.
