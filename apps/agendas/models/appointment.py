# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.postgres.fields import JSONField

from apps.agendas.models.choices import AppointmentStatus, AppointmentSite
from apps.contrib.models.mixins import TimeStampedModelMixin, UUIDPrimaryKeyModelMixin


class Appointment(UUIDPrimaryKeyModelMixin, TimeStampedModelMixin):
    doctor = models.ForeignKey(
        'agendas.DoctorProfile',
        on_delete=models.CASCADE,
        verbose_name=_('Doctor'),
    )
    visitor = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name=_('Visitor'),
    )
    status = models.CharField(
        verbose_name=_('Status'),
        max_length=50,
        choices=AppointmentStatus.choices(),
        default=AppointmentStatus.REQUESTED,
    )
    site = models.CharField(
        verbose_name=_('Site'),
        max_length=50,
        choices=AppointmentSite.choices(),
        default=AppointmentSite.IN_PLACE,
    )
    date = models.DateField(
        verbose_name=_('Date'),
    )
    time = models.TimeField(
        verbose_name=_('Time'),
    )

    consultation_duration = models.PositiveIntegerField(
        verbose_name=_('Duration'),
    )

    # this field is JSON to add more flexibility to appointments
    payload = JSONField(
        encoder=DjangoJSONEncoder,
        verbose_name=_('extra'),
        help_text=_('This field changes according to the type of action'),
        default=dict,
        blank=True,
    )

    def __str__(self):
        return '{0} {1}'.format(self.date, self.time)

    class Meta:
        db_table = 'appointments'
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')
        ordering = ['created_at']
        app_label = 'agendas'
        unique_together = ('doctor', 'visitor', 'date', 'time')
