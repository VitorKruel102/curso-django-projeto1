from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Website homepage."""
    return HttpResponse('HOME')


def contact(request):
    """Contact page."""
    return HttpResponse('Contact')


def about(request):
    """About page."""
    return HttpResponse('About')
