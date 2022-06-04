from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def index(request):
    # todo o processamento acontece aq dentro
    context = {
        'nome': "Ludivik de Paula"
    }

    return render(request, "index.html", context=context)
