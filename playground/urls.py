from django.urls import path
from .views import HelloView

urlpatterns = [
    path("index/", HelloView.as_view(), name="index"),
]
