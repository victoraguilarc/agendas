from rest_framework.exceptions import NotFound

from apps.agendas.models import Appointment
from apps.agendas.response_codes import APPOINTMENT_NOT_FOUND


class AppointmentSelector(object):

    @classmethod
    def get_by_uuid(cls, uuid):
        try:
            Appointment.objects.get(uuid=uuid)
        except Appointment.DoesNotExist:
            raise NotFound(**APPOINTMENT_NOT_FOUND)

    @classmethod
    def user_appointments(cls, user):
        return Appointment.objects.filter(visitor=user)

    @classmethod
    def professional_appointments(cls, doctor):
        return Appointment.objects.filter(doctor=doctor)
