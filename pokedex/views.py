from django.http import HttpResponse
from django.template import loader
from .models import Pokemon , trainer
def index(request):
    pokemons = Pokemon.objects.all()
    trainers = trainer.objects.all()    
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers}, request))

def pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer_details(request, id: int):
    trainer_details = trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer_details
    }
    return HttpResponse(template.render(context, request))