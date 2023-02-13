from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    """Website homepage."""
    template_name = 'recipes/pages/home.html'
    context = {'recipes': [make_recipe() for _ in range(10)]}
    return render(request, template_name, context)

def recipe(request, id):
    """Website homepage."""
    template_name = 'recipes/pages/recipe-view.html'
    context = {'recipe': [make_recipe()]}
    return render(request, template_name, context)

