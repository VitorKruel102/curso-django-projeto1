from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Website homepage."""
    template_name = 'recipes/home.html'
    context = {'name': 'Vitor'}
    return render(request, template_name, context)


def contact(request):
    """Contact page."""
    template_name = 'recipes/contact.html'
    return render(request, template_name)


def about(request):
    """About page."""
    return HttpResponse('About')
