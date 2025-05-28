from django.shortcuts import render
from datetime import datetime

# Create your views here.

def get_banner_data():
    """Fonction utilitaire pour récupérer les données de la bannière"""
    h = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
    name = "Vincent et Kévin"
    return {'hours': h, 'cname': name}

def accueil(request):
    return render(request, 'accueil.html', get_banner_data())

def country_list(request):
    from .models import Country
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

def city_list(request):
    from .models import City
    cities = City.objects.all()
    return render(request, 'city_list.html', {'cities': cities})