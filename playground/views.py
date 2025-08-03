from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from .tasks import notify_customers
import os


def index(request):
    notify_customers.delay("Hello")
    return render(request,"main.html")
