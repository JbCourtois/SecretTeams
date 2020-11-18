from random import Random

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def generate(request, *args, **kwargs):
    game = kwargs.get('game', 1)
    seed = f'{kwargs.get("seed")}{game}'
    rng = Random(seed)

    teams = list(kwargs['teams'])
    rng.shuffle(teams)
    team = teams[kwargs['player']]

    return render(request, "teams.html", {'team': team, 'game': game})
