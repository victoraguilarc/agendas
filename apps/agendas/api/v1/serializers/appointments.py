# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from apps.agendas.models import Appointment


class AppointmentSerializer(ModelSerializer):
    """Serialier to request and validate an email."""

    class Meta:
        model = Appointment
        fields = (
            'agenda',
            'visitor',
            'status',
            'site',
            'start_datetime',
            'duration',
            'payload',
        )
        readonly_fields = fields
