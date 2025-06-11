from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'main.html', {"name": "Django"})
# Create your views here.
