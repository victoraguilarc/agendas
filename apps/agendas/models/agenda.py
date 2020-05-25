# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.contrib.models.mixins import TimeStampedModelMixin


class Agenda(TimeStampedModelMixin):
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
    )
    start_time = models.TimeField(
        verbose_name=_('Start Hour'),
    )

    end_time = models.TimeField(
        verbose_name=_('End Hour'),
    )

    duration = models.IntegerField(
        verbose_name=_('Duration'),
        help_text=_('This time is in minutes'),
    )
    auto_confirmation = models.BooleanField(
        verbose_name=_('Is confirmed automatically?'),
        default=True,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'agendas'
        verbose_name = _('Agenda')
        verbose_name_plural = _('Agendas')
        ordering = ['created_at']
        app_label = 'agendas'
