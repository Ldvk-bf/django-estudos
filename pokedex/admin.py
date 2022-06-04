from django.contrib import admin
from . models import pokemon


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.

admin.site.register(pokemon, PokemonAdmin)
