from django.http import HttpResponse
from django.template import loader
from .models import Pokemon , trainer
from pokedex.forms import PokemonForm
from django.shortcuts import render, redirect

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

def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def edit_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

def delete_pokemon(request, id: int):
    pokemon = Pokemon.objects.get(id=id)
    pokemon.delete()
    return redirect('pokedex:index')