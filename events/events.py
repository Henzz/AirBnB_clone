import uuid
import datetime
import json

class EventManager():
    """The event manager class."""
    def __init__(self):
        self.events = {}

    def create_event(self, event_name, event_date, *notes, **kwargs):
        """creates an event"""
        event_id = str(uuid.uuid4())
        event_datetime = datetime.datetime.strptime(event_date, "%Y-%m-%d %H:%M")
        event_details = {
                "name": event_name,
                "date": event_datetime.strftime("%Y-%m-%d %H:%M"),
                "notes": notes,
                **kwargs
                }
        self.events[event_id] = event_details
        return event_id

    def list_events(self):
        "Displays events created"""
        for event_id, event_details in self.events.items():
            print(f"Event ID is {event_id}")
            print(f"Name of event is {event_details['name']}")
            print(f"Date of event is {event_details['date']}")
            if event_details['notes']:
                print("Notes:")
                for note in event_details['notes']:
                    print(f" - {note}")
            print("AOB:")
            for key, value in event_details.items():
                if key not in ['name', 'date', 'notes']:
                    print(f" - {key}: {value}")
            print()

    def update_event(self, event_id, **kwargs):
        """Updates an event"""
        if event_id in self.events:
            event_details = self.events[event_id]
            event_details.update(kwargs)

    def delete_event(self, event_id):
        """Deletes an event"""
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False

    def save_event(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.events, f)

    def load_events(self, filename):
        try:
            with open(filename, 'r') as f:
                self.events = json.load(f)
        except FileNotFoundError:
            self.events = {}


if __name__ == "__main__":
    events_manager = EventManager()
    """
    events_manager.create_event(
            "1 - C19 Live Learning Session",
            "2024-02-07 15:00",
            "We'll be talking about the AirBnB Clone Project",
            location="via Zoom",
            invitees="Cohort 19 SEs",
            recorded=True)

    events_manager.create_event(
            "2 - C19 Live Learning Session",
            "2022-02-07 15:00",
            "The AirBnB Clone Project",
            location="via Zoom",
            invitees="Cohort 19 SEs",
            recorded=True)
    """
    events_manager.load_events("events.json")
    events_manager.update_event(list(events_manager.events.keys())[1], notes=["New updates."])
    print(list(events_manager.events.keys())[1])

    # events_manager.list_events()
    events_manager.save_event("events.json")
