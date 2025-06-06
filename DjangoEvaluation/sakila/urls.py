from django.urls import path
from django.http import HttpResponse
from sakila.views import accueil, country_list, city_list, city_detail

urlpatterns = [
    path('', accueil, name='accueil'),  # Route racine vers accueil
    path('accueil/', accueil, name='accueil'),
    path('favicon.ico', lambda request: HttpResponse(status=204)),
    path('country/', country_list, name='country_list'),
    path('city/', city_list, name='city_list'),
    path('city/<int:city_id>/', city_detail, name='city_detail'),
]