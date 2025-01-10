from appointment_confirmation_event import AppointmentConfirmationEvent

class Embassy:
    def __init__(self, name, address, phone_number, email, event_queue):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.event_queue = event_queue

    def handle_appointment_request(self, event):
        print(f"Received appointment request for Passport: {event.payload['passport_number']} on {event.payload['date']}")
        confirmation_event = AppointmentConfirmationEvent(event.payload["passport_number"], is_confirmed=True)
        self.event_queue.append(confirmation_event)
        print('Event', confirmation_event.name, 'emitted!')
