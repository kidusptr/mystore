from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import requests
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info("calling httpbin")
            response = requests.get("https://httpbin.org/delay/2")
            logger.info("got response from httpbin")
            data = response.json()
        except requests.ConnectionError:
            logger.critical("could not connect to httpbin")
        return render(request, "main.html", {"name": "Django"})
