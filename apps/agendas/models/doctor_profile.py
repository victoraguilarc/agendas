# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.contrib.models.mixins import TimeStampedModelMixin, UUIDPrimaryKeyModelMixin
from apps.accounts.models.choices import Specialties


class DoctorProfile(UUIDPrimaryKeyModelMixin, TimeStampedModelMixin):
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='doctor_profile',
    )

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

    start_time = models.TimeField(
        verbose_name=_('Start'),
    )

    end_time = models.TimeField(
        verbose_name=_('End'),
    )

    fee = models.DecimalField(
        verbose_name=_('Fee'),
        decimal_places=2,
        max_digits=20,
        help_text=_('This price is for the a session wirh [x] duration in minutes, duration is configured below'),
    )

    consultation_duration = models.IntegerField(
        verbose_name=_('Consultation Duration'),
        help_text=_('This time is in minutes'),
    )

    auto_confirmation = models.BooleanField(
        verbose_name=_('Auto Confirmation?'),
        help_text=_('If it\'s false the doctor must be accept or denied appointments manually'),
        default=True,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'professional_profiles'
        verbose_name = _('Professional')
        verbose_name_plural = _('Professionals')
        app_label = 'agendas'
