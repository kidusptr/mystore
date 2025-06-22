from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):

    product = Product.objects.filter(pk=0).exists()

    return render(request, "main.html", {"name": "Django"})


# Create your views here.
