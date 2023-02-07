from django.urls import path, include

from recipes.views import home, contact, about

urlpatterns = [
    path('', home),
    path('contato/', contact),
    path('sobre/', about),
]
