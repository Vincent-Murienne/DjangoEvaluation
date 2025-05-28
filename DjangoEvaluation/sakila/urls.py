from django.urls import path
from django.http import HttpResponse
from sakila.views import accueil

urlpatterns = [
    path('', accueil, name='accueil'),  # Route racine vers accueil
    path('favicon.ico', lambda request: HttpResponse(status=204)),
]