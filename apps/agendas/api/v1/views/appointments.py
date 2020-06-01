# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.agendas.api.v1.serializers.appointments import CreateAppointmentSerializer, AppointmentSerializer
from apps.agendas.selectors.appointments import AppointmentSelector
from apps.agendas.services.appointments import AppointmentService


class AppointmentsViewSet(ViewSet):
    """Process a google token_id login."""
    permission_classes = [IsAuthenticated]

    def create(self, request, **kwargs):
        serializer = CreateAppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        appointment = AppointmentService.create(
            professional_uuid=serializer.validated_data['professional'],
            visitor=request.user,
            date=serializer.validated_data['date'],
            time=serializer.validated_data['time'],
            site=serializer.validated_data['site'],
        )
        return Response(AppointmentSerializer(appointment).data)

    def retrieve(self, request, appointment_uuid, **kwargs):
        appointment = AppointmentSelector.get_by_uuid(appointment_uuid)
        return Response(AppointmentSerializer(appointment).data)

    def cancel(self, request, **kwargs):
        return Response({'status': 'OK'})

