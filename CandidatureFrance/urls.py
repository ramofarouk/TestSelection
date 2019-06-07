from django.contrib import admin
from django.urls import path, include
from CityChecking.views import *
from GoogleCalendarAdding.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('city-check/', city_check),
    path('add-event/', add_event),
    path('send-success/', send_success),
    path('not-found/', not_found),
    path(r'list-data/<city_name>', list_data, name='list_data'),
]
