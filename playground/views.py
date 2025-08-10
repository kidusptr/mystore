from django.shortcuts import render
from django.core.cache import cache
import requests


def index(request):
    key = "httpbin_result"

    if cache.get(key) is None:
        response = requests.get("https://httpbin.org/get")
        data = response.json()
        cache.set(key, data)
    return render(request, "main.html", {"name": cache.get(key)})
