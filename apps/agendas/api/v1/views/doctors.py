# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.agendas.api.v1.serializers.doctors import DoctorProfileSerializer
from apps.agendas.selectors.doctors import DoctorSelector
from apps.agendas.api.v1.serializers.appointments import AppointmentSerializer
from apps.agendas.selectors.appointments import AppointmentSelector
from apps.agendas.services.doctors import DoctorService
from apps.contrib.api.viewsets import PermissionViewSet
from apps.contrib.utils.casts import clean_int


class DoctorsViewSet(PermissionViewSet):
    permission_classes = [IsAuthenticated]
    permissions_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
    }

    def list(self, request, **kwargs):
        doctors = DoctorSelector.get_enabled_doctors()
        return Response(DoctorProfileSerializer(doctors, many=True).data)

    def retrieve(self, request, doctor_uuid, **kwargs):
        doctor = DoctorSelector.get_by_uuid(doctor_uuid)
        return Response(DoctorProfileSerializer(doctor).data)

    def appointments(self, request, doctor_uuid, **kwargs):
        """It shows the appointments to the professionals."""

        doctor = DoctorSelector.get_by_uuid(doctor_uuid)
        appointments = AppointmentSelector.professional_appointments(doctor)
        return Response(AppointmentSerializer(appointments, many=True).data)

    def calendar(self, request, doctor_uuid, **kwargs):
        week = clean_int(request.query_params.get('week'))
        professional = DoctorSelector.get_by_uuid(doctor_uuid)

        calendar = DoctorService.week_calendar(professional, week=week)
        return Response(calendar)
