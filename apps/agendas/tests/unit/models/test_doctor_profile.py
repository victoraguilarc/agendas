# -*- coding: utf-8 -*-

import pytest

from django.utils.translation import ugettext_lazy as _

from apps.agendas.models import DoctorProfile
from apps.agendas.tests.factories.doctor_profile import DoctorProfileFactory


@pytest.mark.django_db
class DoctorProfileModelTests:

    @staticmethod
    def test_string_representation():
        doctor_profile = DoctorProfileFactory()
        assert str(doctor_profile) == str(doctor_profile.user)

    @staticmethod
    def test_verbose_name():
        assert str(DoctorProfile._meta.verbose_name) == _('Doctor')

    @staticmethod
    def test_verbose_name_plural():
        assert str(DoctorProfile._meta.verbose_name_plural) == _('Doctors')
