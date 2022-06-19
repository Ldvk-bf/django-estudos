from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "Ludivik": "top"
    }
    return render(request, "pokedex/index.html", context)


def addPokemon(request):
    return render(request, "pokedex/add_pokemon.html")
