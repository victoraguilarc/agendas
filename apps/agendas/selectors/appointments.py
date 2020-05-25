
from apps.agendas.models import Appointment


class AppointmentSelector(object):

    @classmethod
    def user_appointments(cls, user):
        return Appointment.objects.filter(visitor=user)

    @classmethod
    def professional_appointments(cls, professional):
        return Appointment.objects.filter(agenda__owner=professional.user)
