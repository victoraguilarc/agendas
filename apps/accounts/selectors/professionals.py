from django.db.models import Q
from rest_framework.exceptions import NotFound

from apps.accounts.models import ProfessionalProfile
from apps.agendas.models import Appointment
from apps.agendas.response_codes import PROFESSIONAL_NOT_FOUND


class ProfessionalSelector(object):

    @classmethod
    def get_active_professionals(cls):
        return ProfessionalProfile.objects.filter(user__is_active=True)

    @classmethod
    def get_by_username_or_email(cls, user_or_email):
        try:
            _filter = Q(user__username=user_or_email) | Q(user__email=user_or_email)
            return ProfessionalProfile.objects.get(_filter)
        except ProfessionalProfile.DoesNotExist:
            raise NotFound(**PROFESSIONAL_NOT_FOUND)
