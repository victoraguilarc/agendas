
from apps.agendas.models import Appointment


class AppointmentSelector(object):

    @classmethod
    def get_professional_appointments(cls, professional):
        return Appointment.objects.filter(agenda__owner=professional.user)
