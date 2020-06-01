from django.db.models import Q
from rest_framework.exceptions import NotFound

from apps.agendas.models import DoctorProfile
from apps.agendas.response_codes import DOCTOR_NOT_FOUND


class DoctorProfileSelector(object):

    @classmethod
    def get_enabled_doctors(cls):
        return DoctorProfile.objects.filter(user__is_active=True)

    @classmethod
    def get_by_username_or_email(cls, user_or_email):
        try:
            _filter = Q(user__username=user_or_email) | Q(user__email=user_or_email)
            return DoctorProfile.objects.get(_filter)
        except DoctorProfile.DoesNotExist:
            raise NotFound(**DOCTOR_NOT_FOUND)

    @classmethod
    def get_by_uuid(cls, doctor_uuid):
        try:
            return DoctorProfile.objects.get(uuid=doctor_uuid)
        except DoctorProfile.DoesNotExist:
            raise NotFound(**DOCTOR_NOT_FOUND)
