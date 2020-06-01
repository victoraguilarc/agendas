# -*- coding: utf-8 -*-
from datetime import time

import factory
from faker import Factory
from faker.providers import lorem

from apps.agendas.models import DoctorProfile
from apps.accounts.tests.factories.user import UserFactory

faker = Factory.create()
faker.add_provider(lorem)


class DoctorProfileFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    title = factory.LazyFunction(faker.word)
    location = factory.LazyFunction(faker.sentence)

    start_time = factory.LazyAttribute(lambda x: time(8, 0))
    end_time = factory.LazyAttribute(lambda x: time(12, 0))
    fee = 100
    consultation_duration = 30

    class Meta:
        model = DoctorProfile
