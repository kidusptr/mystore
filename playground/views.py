from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection, Product
from tags.models import TaggedItem


# Create your views here.
