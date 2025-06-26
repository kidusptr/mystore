from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection, Product
from tags.models import TaggedItem


def say_hello(request):
    try:
        Collection.objects.filter(pk=12).delete()
        queryset = Collection.objects.all()
    except ObjectDoesNotExist:
        return render(request, "errors.html")

    return render(
        request,
        "main.html",
        {"name": "Django", "collections": list(queryset)},
    )


# Create your views here.
