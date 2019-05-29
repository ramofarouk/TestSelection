import httplib2
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from googleapiclient import discovery
from oauth2client import tools
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage


def add_event(request):
    if request.method == 'POST':
        form_valid()
        return redirect('/add-event/')
    else:
        return render(request, "add-event.html")


# ---------------------------------------------------------------------------
# google_calendar_connection
# ---------------------------------------------------------------------------
def google_calendar_connection():
    flags = tools.argparser.parse_args([])
    flow = OAuth2WebServerFlow(
        client_id='885650566355-dh7b646frijk6g8229bpq6c5oo2bsuan.apps.googleusercontent.com',
        client_secret='m88jox8HcjxFzfoAS9SnI7Q5',
        scope='https://www.googleapis.com/auth/calendar',
        user_agent='<application name>'
    )
    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid is True:
        credentials = tools.run_flow(flow, storage, flags)

        # Create an httplib2.Http object to handle our HTTP requests and authorize it
        # with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = discovery.build('calendar', 'v3', http=http)

    return service


def form_valid():
    """
    This method used for add event in google calendar.
    """
    service = google_calendar_connection()
    event = {
        'summary': "new",
        'location': "london",
        'description': "anything",
        'start': {
            'date': "2019-07-02",
        },
        'end': {
            'date': "2019-09-02",
        },
    }

    event_request = service.events().insert(calendarId='primary', body=event).execute()
    print(event_request)
    # return CreateView.form_valid(self,form)
