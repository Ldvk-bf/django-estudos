from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "pokedex/index.html")


def addPokemon(request):
    return render(request, "pokedex/add_pokemon.html")
