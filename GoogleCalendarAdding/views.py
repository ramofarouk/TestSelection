import httplib2
from django.shortcuts import render, redirect

# Create your views here.
from googleapiclient import discovery
from oauth2client import tools
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
import datetime


# Vue pour la page de saisie des informations
def add_event(request):
    if request.method == 'POST':
        date = request.POST["date"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        title = request.POST["title"]
        description = request.POST["description"]
        form_valid(date, time_start, time_end, title, description)
        return redirect('/send-success/')
    else:
        return render(request, "add-event.html")


# Vue pour le message de succès
def send_success(request):
    return render(request, "send-success.html")


# ---------------------------------------------------------------------------
# Fonction pour la connexion au Google Calendar
# ---------------------------------------------------------------------------
def google_calendar_connection():
    flags = tools.argparser.parse_args([])
    flow = OAuth2WebServerFlow(
        # Remplacer avec votre client_id
        client_id='votre_id_client.apps.googleusercontent.com',
        client_secret='client_secret',  # Remplacer avec votre client_secret
        scope='https://www.googleapis.com/auth/calendar',
        user_agent='<application name>'
    )
    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid is True:
        credentials = tools.run_flow(flow, storage, flags)

    http = httplib2.Http()
    http = credentials.authorize(http)
    service = discovery.build('calendar', 'v3', http=http)

    return service


# Fonction pour l'envoi des données au Google Calendar
def form_valid(date, time_start, time_end, title, description):
    """
    This method used for add event in google calendar.
    """
    service = google_calendar_connection()  # Connexion
    date_time_start_str = date + 'T' + time_start + ':00+00:00'  # Conversion pour la date et heure de début
    date_time_end_str = date + 'T' + time_end + ':00+00:00'  # Conversion pour la date et heure de fin
    event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': date_time_start_str,
        },
        'end': {
            'dateTime': date_time_end_str,
        },
        'organizer': {
            'email': 'omarharden228@gmail.com',
            'self': False
        },
        'creator': {
            'email': 'omarharden228@gmail.com',
            'self': False
        },

    }

    event_request = service.events().insert(calendarId='primary', body=event).execute()  # Exécution
    print(event_request)
