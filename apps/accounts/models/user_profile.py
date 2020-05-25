# -*- coding: utf-8 -*-

from django.db import models

from apps.contrib.models.mixins import TimeStampedModelMixin
from apps.accounts.models.choices import Specialties

from django.utils.translation import ugettext_lazy as _


class UserProfile(TimeStampedModelMixin):

    specialty = models.CharField(
        max_length=25,
        choices=Specialties.choices(),
        default=Specialties.GENERAL_DOCTOR,
    )

    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='user_profile',
    )

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'user_profiles'
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
        app_label = 'accounts'
