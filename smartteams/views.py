from random import Random

from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)

from smartteams.forms import GenerateForm


def index(request):
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            seed = form.cleaned_data['seed']
            teams = form.cleaned_data['teams']
            return HttpResponseRedirect(f'{seed}/{teams}/0/1')
    else:
        form = GenerateForm()

    return render(request, 'smartteams/index.html', {'form': form})


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
