from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests


@cache_page(5 * 60)
def index(request):
    response = requests.get("https://httpbin.org/get")
    data = response.json()
    return render(request, "main.html", {"name": data})
