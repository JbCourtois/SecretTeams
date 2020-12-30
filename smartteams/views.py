from random import Random

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "smartteams/index.html")


def generate(request, *args, **kwargs):
    game = kwargs.get('game', 1)
    seed = kwargs.get('seed', '')
    rng = Random(f'{seed}{game}')

    teams = list(kwargs['teams'])
    rng.shuffle(teams)
    team = teams[kwargs['player']]

    return render(request, "smartteams/teams.html", {
        'team': team,
        'game': game,
        'seed': seed,
    })
