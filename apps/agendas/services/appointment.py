# -*- coding: utf-8 -*-
from django.db import IntegrityError

from apps.agendas.selectors.doctor_profile import DoctorProfileSelector
from apps.agendas.models import Appointment, AppointmentSite, AppointmentStatus
from apps.agendas.response_codes import UNAVAILABLE_DATETIME
from apps.contrib.api.exceptions import SimpleValidationError


class AppointmentService(object):

    @classmethod
    def create(cls, doctor_uuid, visitor, date, time, site=AppointmentSite.IN_PLACE):
        doctor = DoctorProfileSelector.get_by_uuid(doctor_uuid)
        status = AppointmentStatus.ACCEPTED if doctor.auto_confirmation else AppointmentStatus.REQUESTED

        try:
            return Appointment.objects.create(
                consultation_duration=doctor.consultation_duration,
                doctor=doctor,
                visitor=visitor,
                site=site,
                status=status,
                date=date,
                time=time,
            )
        except IntegrityError:
            raise SimpleValidationError(**UNAVAILABLE_DATETIME)
