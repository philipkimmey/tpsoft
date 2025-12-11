from django.shortcuts import render
from django.utils import timezone


def home(request):
    return render(request, "web/home.html")


def ping(request):
    context = {
        "timestamp": timezone.now(),
    }
    return render(request, "web/partials/ping_response.html", context)
