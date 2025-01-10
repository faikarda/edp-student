from embassy_appointment_request_event import EmbassyAppointmentRequestEvent

class Student:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number, passport_number, event_queue):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.passport_number = passport_number
        self.event_queue = event_queue

    def ask_for_embassy_appointment(self, date):
        event = EmbassyAppointmentRequestEvent(self.passport_number, date)
        self.event_queue.append(event)
        print('Event', event.name, 'emitted!')

    def handle_appointment_confirmation(self, event):
        if event.payload['is_confirmed']:
            print("Awesome. I have an appointment at Polish Embassy")
        else:    
            print("Oh no! I will have to try again")
