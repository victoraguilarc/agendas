# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.agendas.models.doctor_profile import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'specialty',
        'verified',
        'start_time',
        'end_time',
        'consultation_duration',
        'auto_confirmation',
    )
    search_fields = ('user__email', 'user__username')
    raw_id_fields = ('user', )
    list_filter = ('specialty', 'location', 'verified')
