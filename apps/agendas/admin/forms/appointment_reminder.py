from django import forms

from apps.agendas.models import Appointment
from apps.agendas.services.appointment import AppointmentService


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentReminderForm(AppointmentForm):

    def form_action(self, appointment):
        AppointmentService.send_reminder(appointment)
