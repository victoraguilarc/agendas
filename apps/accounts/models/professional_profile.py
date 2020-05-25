# -*- coding: utf-8 -*-

from django.db import models

from apps.contrib.models.mixins import TimeStampedModelMixin
from apps.accounts.models.choices import Specialties

from django.utils.translation import ugettext_lazy as _


class ProfessionalProfile(TimeStampedModelMixin):

    specialty = models.CharField(
        max_length=25,
        choices=Specialties.choices(),
        default=Specialties.GENERAL_DOCTOR,
    )

    title = models.TextField(
        verbose_name=_('Title'),
    )

    location = models.CharField(
        verbose_name=_('Locatión'),
        max_length=255,
        blank=True, null=True,
    )

    verified = models.BooleanField(
        verbose_name=_('Is verified?'),
        default=False,
    )

    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='user_profile',
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'professional_profiles'
        verbose_name = _('Professional')
        verbose_name_plural = _('Professionals')
        app_label = 'accounts'
