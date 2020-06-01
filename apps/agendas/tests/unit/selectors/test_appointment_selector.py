# -*- coding: utf-8 -*-

import pytest
from django.db.models import QuerySet
from rest_framework.exceptions import NotFound

from apps.agendas.models import Appointment
from apps.agendas.response_codes import APPOINTMENT_NOT_FOUND
from apps.agendas.selectors.appointment import AppointmentSelector
from apps.agendas.tests.factories.appointment import AppointmentFactory
from apps.agendas.tests.factories.doctor_profile import DoctorProfileFactory

from faker import Factory
from faker.providers import misc


faker = Factory.create()
faker.add_provider(misc)


@pytest.mark.django_db
class AppointmentSelectorTests:

    @staticmethod
    def test_get_by_uuid():
        appointment = AppointmentFactory()
        selected_appointment = AppointmentSelector.get_by_uuid(str(appointment.uuid))
        assert isinstance(selected_appointment, Appointment)
        assert selected_appointment == appointment

    @staticmethod
    def test_get_by_uuid_not_found():
        with pytest.raises(NotFound) as exec_info:
            AppointmentSelector.get_by_uuid(faker.uuid4())
        assert exec_info.value.detail.code == APPOINTMENT_NOT_FOUND['code']

    @staticmethod
    def test_user_appointments(test_user):
        doctor_profile = DoctorProfileFactory()
        user_appointment = AppointmentFactory(visitor=test_user)
        AppointmentFactory(doctor=doctor_profile)

        queryset = AppointmentSelector.user_appointments(test_user)
        assert isinstance(queryset, QuerySet)
        assert queryset.count() == 1
        assert queryset.first() == user_appointment

    @staticmethod
    def test_user_appointments_empty(test_user):
        doctor_profile = DoctorProfileFactory()
        AppointmentFactory(doctor=doctor_profile)
        queryset = AppointmentSelector.user_appointments(test_user)
        assert isinstance(queryset, QuerySet)
        assert queryset.count() == 0

    @staticmethod
    def test_doctor_appointments(test_user):
        doctor_profile = DoctorProfileFactory()
        AppointmentFactory(visitor=test_user)
        doctor_appointment = AppointmentFactory(doctor=doctor_profile)

        queryset = AppointmentSelector.doctor_appointments(doctor_profile)
        assert isinstance(queryset, QuerySet)
        assert queryset.count() == 1
        assert queryset.first() == doctor_appointment

    @staticmethod
    def test_doctor_appointments_empty(test_user):
        doctor_profile = DoctorProfileFactory()
        AppointmentFactory(visitor=test_user)
        queryset = AppointmentSelector.doctor_appointments(doctor_profile)
        assert isinstance(queryset, QuerySet)
        assert queryset.count() == 0

