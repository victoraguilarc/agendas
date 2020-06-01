# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.agendas.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'status',
        'date',
        'time',
        'consultation_duration',
    )
    raw_id_fields = ('doctor', 'visitor')

