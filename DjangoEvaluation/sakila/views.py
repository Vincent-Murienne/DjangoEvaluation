from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import base64
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
    
    # Récupérer le paramètre de filtre
    filter_type = request.GET.get('filter', 'all')
    
    if filter_type == 'capitals':
        cities = City.objects.filter(capital=True)
    else:
        cities = City.objects.all()
    
    return render(request, 'city_list.html', {
        'cities': cities,
        'current_filter': filter_type
    })

def city_detail(request, city_id):
    from .models import City
    
    city = get_object_or_404(City, city_id=city_id)
    
    # Convertir l'image en base64 si elle existe
    image_data = None
    if city.picture:
        image_data = base64.b64encode(city.picture).decode('utf-8')
    
    return render(request, 'city_detail.html', {
        'city': city,
        'image_data': image_data
    })