# -*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.accounts.api.v1.serializers.professionals import ProfessionalSerializer
from apps.accounts.selectors.professionals import ProfessionalSelector
from apps.agendas.api.v1.serializers.appointments import AppointmentSerializer
from apps.agendas.selectors.appointments import AppointmentSelector
from apps.contrib.api.viewsets import PermissionViewSet


class ProfessionalsViewSet(PermissionViewSet):
    permission_classes = [IsAuthenticated]
    permissions_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
    }

    def list(self, request, **kwargs):
        professionals = ProfessionalSelector.get_active_professionals()
        return Response(ProfessionalSerializer(professionals, many=True).data)

    def retrieve(self, request, professional_uuid, **kwargs):
        professional = ProfessionalSelector.get_by_uuid(professional_uuid)
        return Response(ProfessionalSerializer(professional).data)

    def appointments(self, request, professional_uuid, **kwargs):
        """It shows the appointments to the professionals."""

        professional = ProfessionalSelector.get_by_uuid(professional_uuid)
        appointments = AppointmentSelector.professional_appointments(professional)
        return Response(AppointmentSerializer(appointments, many=True).data)

    def calendar(self, request, professional_uuid, **kwargs):
        return Response({'status': 'OK'})
