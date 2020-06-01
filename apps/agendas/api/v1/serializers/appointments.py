# -*- coding: utf-8 -*-

from rest_framework import serializers
from apps.agendas.models import Appointment, AppointmentSite


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    visitor = serializers.SerializerMethodField()

    def get_doctor(self, appointment):
        return {
            'uuid': appointment.doctor.uuid,
            'full_name': appointment.doctor.user.full_name,
            'email': appointment.doctor.user.email,
        }

    def get_visitor(self, appointment):
        return {
            'full_name': appointment.visitor.full_name,
            'email': appointment.visitor.email,
        }

    class Meta:
        model = Appointment
        fields = (
            'doctor',
            'visitor',
            'status',
            'site',
            'date',
            'time',
            'consultation_duration',
            'payload',
        )
        read_only_fields = fields


class CreateAppointmentSerializer(serializers.Serializer):
    doctor_uuid = serializers.UUIDField()
    date = serializers.DateField()
    time = serializers.TimeField()
    site = serializers.ChoiceField(
        AppointmentSite.choices(),
        default=AppointmentSite.IN_PLACE,
    )
