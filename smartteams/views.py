from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def generate(request, *args, **kwargs):
    return render(request, "teams.html", {'game': kwargs.get('game', 1)})
