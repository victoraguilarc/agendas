# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.agendas.api.v1.serializers.appointments import CreateAppointmentSerializer, AppointmentSerializer
from apps.agendas.selectors.appointment import AppointmentSelector
from apps.agendas.selectors.doctor_profile import DoctorProfileSelector
from apps.agendas.services.appointment import AppointmentService
from apps.agendas.services.doctor_profile import DoctorProfileService


class AppointmentsViewSet(ViewSet):
    """Process a google token_id login."""
    permission_classes = [IsAuthenticated]

    def create(self, request, **kwargs):
        serializer = CreateAppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        appointment = AppointmentService.create(
            serializer.validated_data['doctor_uuid'],
            visitor=request.user,
            date=serializer.validated_data['date'],
            time=serializer.validated_data['time'],
            site=serializer.validated_data['site'],
        )
        week = DoctorProfileService.get_week_number(
            serializer.validated_data['date'],
            serializer.validated_data['time'],
        )
        doctor = DoctorProfileSelector.get_by_uuid(serializer.validated_data['doctor_uuid'])
        week_days = DoctorProfileService.week_calendar(doctor, week=week)
        return Response({
            'appointment': AppointmentSerializer(appointment).data,
            'week_days': week_days
        })

    def retrieve(self, request, appointment_uuid, **kwargs):
        appointment = AppointmentSelector.get_by_uuid(appointment_uuid)
        return Response(AppointmentSerializer(appointment).data)

    def cancel(self, request, **kwargs):
        return Response({'status': 'OK'})

