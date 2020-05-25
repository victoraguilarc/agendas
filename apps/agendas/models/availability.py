# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.contrib.models.mixins import TimeStampedModelMixin


class DayAvailability(TimeStampedModelMixin):
    agenda = models.ForeignKey(
        'agendas.Agenda',
        on_delete=models.CASCADE,
    )
    day = models.DateField(
        verbose_name=_('Day')
    )

    start_hour = models.IntegerField(
        verbose_name=_('Start Hour'),
    )
    end_hour = models.IntegerField(
        verbose_name=_('Start Hour'),
    )


