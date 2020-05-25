# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.postgres.fields import JSONField

from apps.agendas.models.choices import AppointmentStatus, AppointmentSite
from apps.contrib.models.mixins import TimeStampedModelMixin, UUIDPrimaryKeyModelMixin


class Appointment(UUIDPrimaryKeyModelMixin, TimeStampedModelMixin):
    agenda = models.ForeignKey(
        'Agenda',
        on_delete=models.CASCADE,
        verbose_name=_('Agenda'),
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
    start_datetime = models.DateTimeField(
        verbose_name=_('Start'),
    )
    duration = models.PositiveIntegerField(
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
        return str(self.start_datetime)

    class Meta:
        db_table = 'appointments'
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')
        ordering = ['created_at']
        app_label = 'agendas'
