# -*- coding: utf-8 -*-

import pytest

from django.utils.translation import ugettext_lazy as _

from apps.agendas.models import Appointment
from apps.agendas.tests.factories.appointment import AppointmentFactory


@pytest.mark.django_db
class AppointmentModelTests:

    @staticmethod
    def test_string_representation():
        appointment = AppointmentFactory()
        assert str(appointment) == '{0} {1}'.format(appointment.date, appointment.time)

    @staticmethod
    def test_verbose_name():
        assert str(Appointment._meta.verbose_name) == _('Appointment')

    @staticmethod
    def test_verbose_name_plural():
        assert str(Appointment._meta.verbose_name_plural) == _('Appointments')
