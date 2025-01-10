from event import Event

class EmbassyAppointmentRequestEvent(Event):
    def __init__(self, passport_number, date):
        super().__init__("embassy_appointment_request", {"passport_number": passport_number, "date": date})