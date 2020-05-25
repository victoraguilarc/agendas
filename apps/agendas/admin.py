# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.agendas.models import Agenda, Appointment


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'start_time',
        'end_time',
        'duration',
        'auto_confirmation',
    )
    raw_id_fields = ('user', )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'schedule',
        'status',
        'start_datetime',
        'duration',
    )

