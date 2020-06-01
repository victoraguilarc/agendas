# -*- coding: utf-8 -*-
from django.db import IntegrityError

from apps.agendas.selectors.professionals import DoctorSelector
from apps.agendas.models import Appointment, AppointmentSite
from apps.agendas.response_codes import UNAVAILABLE_DATETIME
from apps.contrib.api.exceptions import SimpleValidationError


class AppointmentService(object):

    @classmethod
    def create(cls, professional_uuid, visitor, date, time, site=AppointmentSite.IN_PLACE):
        doctor = DoctorSelector.get_by_uuid(professional_uuid)

        try:
            return Appointment.objects.create(
                consultation_duration=doctor.consultation_duration,
                doctor=doctor,
                visitor=visitor,
                site=site,
                date=date,
                time=time,
            )
        except IntegrityError:
            raise SimpleValidationError(**UNAVAILABLE_DATETIME)
