# -*- coding: utf-8 -*-

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from django.utils.html import format_html

from apps.agendas.models import Appointment
from apps.agendas.services.appointment import AppointmentService


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'visitor',
        'status',
        'date',
        'time',
        'appointment_actions',
    )
    raw_id_fields = ('doctor', 'visitor')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<uuid:appointment_uuid>/reminder/',
                self.admin_site.admin_view(self.process_reminder),
                name='appointment-reminder',
            ),
        ]
        return custom_urls + urls

    def process_reminder(self, request, appointment_uuid, *args, **kwargs):
        appointment = self.get_object(request, appointment_uuid)
        AppointmentService.send_reminder(appointment)

        self.message_user(request, 'Reminder sended to {0}!'.format(appointment.visitor.email))
        url = reverse(
            'admin:agendas_appointment_changelist',
            current_app=self.admin_site.name,
        )
        return HttpResponseRedirect(url)

    def appointment_actions(self, appointment):
        return format_html(
            '<a class="button" href="{}">Send Reminder</a>&nbsp;',
            reverse('admin:appointment-reminder', args=[appointment.uuid]),
        )

    appointment_actions.short_description = 'Actions'
    appointment_actions.allow_tags = True

