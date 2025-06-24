from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem, Order


def say_hello(request):
    try:
        # queryset = Product.objects.defer("description")
        # queryset = (
        #     Product.objects.prefetch_related("promotions")
        #     .select_related("collection")
        #     .all()
        # )
        queryset = (
            Order.objects.select_related("customer")
            .prefetch_related("orderitem_set__product")
            .order_by("-placed_at")[:5]
        )
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "orders": list(queryset)})


# Create your views here.
