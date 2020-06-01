# -*- coding: utf-8 -*-
from datetime import time

import factory
from django.utils.timezone import now
from faker import Factory
from faker.providers import misc, lorem

from apps.accounts.tests.factories.user import UserFactory
from apps.agendas.models import Appointment
from apps.agendas.tests.factories.doctor_profile import DoctorProfileFactory

faker = Factory.create()
faker.add_provider(misc)
faker.add_provider(lorem)


class AppointmentFactory(factory.DjangoModelFactory):
    doctor = factory.SubFactory(DoctorProfileFactory)
    visitor = factory.SubFactory(UserFactory)
    date = factory.LazyAttribute(lambda x: now().date())
    time = factory.LazyAttribute(lambda x: time(8, 0))
    consultation_duration = 30

    class Meta:
        model = Appointment
