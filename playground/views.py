from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Sum, Avg, Max, Min
from store.models import Product, OrderItem, Order


def say_hello(request):
    try:
        # queryset = Product.objects.defer("description")
        # queryset = (
        #     Product.objects.prefetch_related("promotions")
        #     .select_related("collection")
        #     .all()
        # )
        # queryset = (
        #     Order.objects.select_related("customer")
        #     .prefetch_related("orderitem_set__product")
        #     .order_by("-placed_at")[:5]
        # )

        result = Product.objects.aggregate(
            count=Count("id"),
            min_price=Min("unit_price"),
            max_price=Max("unit_price"),
            avg_price=Avg("unit_price"),
        )

    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "result": result})


# Create your views here.
