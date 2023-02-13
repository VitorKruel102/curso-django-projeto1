from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Website homepage."""
    template_name = 'recipes/pages/home.html'
    context = {'name': 'Vitor'}
    return render(request, template_name, context)

def recipe(request, id):
    """Website homepage."""
    template_name = 'recipes/pages/recipe-view.html'
    context = {'name': 'Vitor'}
    return render(request, template_name, context)

