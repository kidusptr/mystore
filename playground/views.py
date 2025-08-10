from django.shortcuts import render
import requests


def index(request):
    requests.get("https://httpbin.org/delay/2")
    return render(request, "main.html", {"name": "Django"})
