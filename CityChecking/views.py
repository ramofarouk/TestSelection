import json
import requests
import simplejson as simplejson
from django.http import HttpResponse
from django.shortcuts import render

from CityChecking.forms import CityForm
from CityChecking.models import *


def home(request):
    return render(request, "index.html")


def city_check(request):
    if request.method == 'POST':
        return render(request, "list-data.html")
    else:
        return render(request, "city-check.html")


def loading_data(request):
    url = 'https://geo.api.gouv.fr/departements/01/communes'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    else:
        weather_data = []
        r = requests.get(url).json()
        commune_info = {
            'commune': r[0],
            'population': r[1],
            'code': r[2],
        }

        weather_data.append(commune_info)
        context = {'weather_data': weather_data}
    return HttpResponse(context, mimetype='application/json')


def index(request):
    url = 'https://geo.api.gouv.fr/departements/01/communes'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    else:
        weather_data = []
        r = requests.get(url).json()
        commune_info = {
            'commune': r[0],
            'population': r[1],
            'code': r[2],
        }

        weather_data.append(commune_info)

    context = {'weather_data': weather_data}
    return render(request, 'index.html', context)
