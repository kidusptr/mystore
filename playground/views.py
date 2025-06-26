from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    try:

        queryset = TaggedItem.objects.get_tags_for(Product, 1)

    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(request, "main.html", {"name": "Django", "result": list(queryset)})


# Create your views here.
