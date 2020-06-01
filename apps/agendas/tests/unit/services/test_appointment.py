# -*- coding: utf-8 -*-
from datetime import time

import pytest
from django.utils.timezone import now

from apps.agendas.models import Appointment
from apps.agendas.response_codes import UNAVAILABLE_DATETIME
from apps.agendas.services.appointment import AppointmentService
from apps.agendas.tests.factories.doctor_profile import DoctorProfileFactory
from apps.contrib.api.exceptions import SimpleValidationError


@pytest.mark.django_db
class AppointmentServiceTests:

    def shared_data(self, test_user):
        doctor_profile = DoctorProfileFactory()
        return {
            'doctor_uuid': str(doctor_profile.uuid),
            'visitor': test_user,
            'date': now().date(),
            'time': time(8, 0),
        }

    def test_create(self, test_user):
        appointment = AppointmentService.create(**self.shared_data(test_user))
        assert isinstance(appointment, Appointment)

    def test_create_unavailable_datetime(self, test_user):
        shared_data = self.shared_data(test_user)
        appointment = AppointmentService.create(**shared_data)
        assert isinstance(appointment, Appointment)

        with pytest.raises(SimpleValidationError) as exec_info:
            AppointmentService.create(**shared_data)
        assert exec_info.value.detail.code == UNAVAILABLE_DATETIME['code']
