# calendar_integration.py

from google.oauth2 import service_account
from googleapiclient.discovery import build

def add_event(event_datetime):
    print(f"Attempting to add event on {event_datetime}")
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    try:
        credentials = service_account.Credentials.from_service_account_file('credentials/credentials.json', scopes=SCOPES)
        print("Google credentials loaded.")
        service = build('calendar', 'v3', credentials=credentials)
        print("Google Calendar service built.")

        event = {
            'summary': 'ERP Demo',
            'location': 'Virtual Meeting',
            'description': 'Demo scheduled by AI agent.',
            'start': {
                'dateTime': event_datetime,
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': event_datetime,
                'timeZone': 'UTC',
            }
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Demo scheduled: {event.get('htmlLink')}")
    except Exception as e:
        print(f"An error occurred while adding the event: {e}")

if __name__ == "__main__":
    # Test the add_event function independently
    test_datetime = "2023-10-27T11:00:00"
    add_event(test_datetime)
