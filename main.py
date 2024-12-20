class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class EmbassyAppointmentRequestEvent(Event):
    def __init__(self, passport_number, date):
        super().__init__("embassy_appointment_request", {"passport_number": passport_number, "date": date})

class AppointmentConfirmationEvent(Event):
    def __init__(self, passport_number, is_confirmed):
        super().__init__("appointment_confirmation", {"passport_number": passport_number, "is_confirmed": is_confirmed})

event_queue = []

class Student:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.passport_number = passport_number

    def ask_for_embassy_appointment(self, date):
        event = EmbassyAppointmentRequestEvent(self.passport_number, date)
        event_queue.append(event)
        print('Event', event.name, 'emitted!')

    def handle_appointment_confirmation(self, event):
        if event.payload['is_confirmed']:
            print("Awesome. I have an appointment at Polish Embassy")
        else:    
            print("Oh no! I will have to try again")

class Embassy:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def handle_appointment_request(self, event):
        print(f"Received appointment request for Passport: {event.payload['passport_number']} on {event.payload['date']}")
        confirmation_event = AppointmentConfirmationEvent(event.payload["passport_number"], is_confirmed=True)
        event_queue.append(confirmation_event)
        print('Event', confirmation_event.name, 'emitted!')
        
# Example Usage
student1 = Student("Piotr1", "Brudny", '1.02.1984', 'Ankara', '5435345345', 'ED4234323')
polish_embassy = Embassy('Polish Embassy', 'Ankara, Harika 10', '343242344', 'polishembassy@gov.tr')


student1.ask_for_embassy_appointment('10.12.2024')

while event_queue: # it runs as long as there is an event in the list
    event = event_queue.pop(0) # takes the event from the top

    # matches events with the handler
    if isinstance(event, EmbassyAppointmentRequestEvent):
        polish_embassy.handle_appointment_request(event) 
    elif isinstance(event, AppointmentConfirmationEvent):
        student1.handle_appointment_confirmation(event)

    