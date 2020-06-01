# -*- coding: utf-8 -*-

import pytest
from django.db.models import QuerySet
from rest_framework.exceptions import NotFound

from apps.accounts.response_codes import INVALID_TOKEN
from apps.accounts.selectors.pending_action_selector import PendingActionSelector
from apps.accounts.tests.factories.pending_action import PendingActionFactory
from apps.accounts.tests.factories.user import UserFactory
from apps.agendas.models import DoctorProfile
from apps.agendas.response_codes import DOCTOR_NOT_FOUND
from apps.agendas.selectors.appointment import AppointmentSelector
from apps.agendas.selectors.doctor_profile import DoctorProfileSelector
from apps.agendas.tests.factories.doctor_profile import DoctorProfileFactory
from apps.contrib.api.exceptions import SimpleValidationError

from faker import Factory
from faker.providers import misc


faker = Factory.create()
faker.add_provider(misc)


@pytest.mark.django_db
class DoctorProfileSelectorTests:

    @staticmethod
    def test_get_by_uuid():
        doctor_profile = DoctorProfileFactory()
        selected_doctor_profile = DoctorProfileSelector.get_by_uuid(str(doctor_profile.uuid))
        assert isinstance(doctor_profile, DoctorProfile)
        assert selected_doctor_profile == doctor_profile

    @staticmethod
    def test_get_by_uuid_not_found():
        with pytest.raises(NotFound) as exec_info:
            DoctorProfileSelector.get_by_uuid(faker.uuid4())
        assert exec_info.value.detail.code == DOCTOR_NOT_FOUND['code']

    @staticmethod
    def test_get_enabled_doctors(test_user):
        inactive_user = UserFactory(is_active=False)
        active_doctor = DoctorProfileFactory(user=test_user)
        DoctorProfileFactory(user=inactive_user)

        doctors = DoctorProfileSelector.get_enabled_doctors()
        assert isinstance(doctors, QuerySet)
        assert doctors.count() == 1
        assert doctors.first() == active_doctor

    @staticmethod
    def test_get_enabled_doctors_empty():
        inactive_user = UserFactory(is_active=False)
        DoctorProfileFactory(user=inactive_user)
        doctors = DoctorProfileSelector.get_enabled_doctors()
        assert isinstance(doctors, QuerySet)
        assert doctors.count() == 0

    def test_get_by_username_or_email(self):
        pass

    def test_get_by_username_or_email_not_found(self):
        pass

