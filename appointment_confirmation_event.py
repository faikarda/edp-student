from event import Event

class AppointmentConfirmationEvent(Event):
    def __init__(self, passport_number, is_confirmed):
        super().__init__("appointment_confirmation", {"passport_number": passport_number, "is_confirmed": is_confirmed})
