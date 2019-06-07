import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from CityChecking.forms import CityForm


# Vue pour la page d'accueil
def index(request):
    return render(request, 'index.html')


# Vue pour la page disant qu'aucune ville n'été trouvé
def not_found(request):
    return render(request, 'not-found.html')


# Vue pour la page de saisie de la ville
def city_check(request):
    if request.method == 'POST':  # Si l'utilisateur  a renseigné une ville
        city_name = request.POST["city_name"]
        return redirect('list_data', city_name=city_name)
    else:
        return render(request, "city-check2.html")


# Vue pour la page affichant les infos d'une ville
def list_data(request, city_name):
    url = 'https://geo.api.gouv.fr/communes?nom=' + city_name + '&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population,centre&format=json&geometry=centre'
    r = requests.get(url).json()
    if len(r) == 0:
        return redirect('/not-found/')
    else:
        city_info = {
            'city_name': r[0]['nom'],
            'latitude': r[0]['centre']['coordinates'][1],
            'longitude': r[0]['centre']['coordinates'][0],
            'people_count': r[0]['population'],
        }

        context = {'city_info': city_info}
        print(context)
        return render(request, 'list-data.html', context)

