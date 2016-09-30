from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class googlecalendar:

    def __init__(self):
        pass

    
    def get_credentials(self):
        """Gets valid user credentials from storage.
    
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
    
        Returns:
        Credentials, the obtained credential.
        """
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        CLIENT_SECRET_FILE = 'client_secret.json'
        APPLICATION_NAME = 'UCSB Calendar'
    
        try:
            import argparse
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None
    
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'calendar-python-quickstart.json')

        store = oauth2client.file.Storage(credential_path)
        self.credentials = store.get()
        if not self.credentials or self.credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                self.credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                self.credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=self.http)
        return self.credentials

    def add_event (self, starttime, endtime, summary, location="", desc="", repeat='RRULE:FREQ=DAILY;COUNT=1'):
        
        event = {
          'summary': summary,
          'location': location,
          'description': desc,
          'start': {
            #'dateTime': '2016-09-29T09:00:00-07:00',
            'dateTime': starttime,
            'timeZone': 'America/Los_Angeles',
          },
          'end': {
            #'dateTime': '2016-09-29T17:00:00-07:00',
            'dateTime': endtime,
            'timeZone': 'America/Los_Angeles',
          },
          'recurrence': [
            repeat
          ],
         # 'attendees': [
         #   {'email': 'lpage@example.com'},
         #   {'email': 'sbrin@example.com'},
         # ],
          'reminders': {
            'useDefault': False,
            #'overrides': [
            #  {'method': 'email', 'minutes': 24 * 60},
            #  {'method': 'popup', 'minutes': 10},
            #],
          },
        }

        event = self.service.events().insert(calendarId='primary', body=event).execute()

    def add_event_ten_weeks (self, starttime, endtime, summary, location="", desc=""):
        self.add_event (starttime, endtime, summary, location, desc,  'RRULE:FREQ=WEEKLY;COUNT=10')


#obj = googlecalendar ()
#obj.get_credentials()
#obj.add_event('2016-10-14T09:00:00', '2016-10-14T11:00:00', 'Test')
#obj.add_event_ten_weeks('2016-11-14T09:00:00', '2016-11-14T11:00:00', 'Test2')
