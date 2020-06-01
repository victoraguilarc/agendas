# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import IntegrityError
from django.urls import reverse

from apps.accounts.emails import ConfirmEmailMessage
from apps.agendas.emails import AppointmentEmailMessage
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

    @classmethod
    def send_reminder(cls, appointment, hostname=settings.PROJECT_HOSTNAME):
        """Sends appointment confirmation email."""
        action_url = reverse('agendas:profile')
        action_url = '{0}{1}'.format(hostname, action_url)
        context = {
            'doctor': appointment.doctor.user.full_name,
            'date': appointment.date,
            'time': appointment.time,
            'note': appointment.note,
            'action_url': action_url,
        }
        AppointmentEmailMessage(context=context).send(to=appointment.visitor.email)
