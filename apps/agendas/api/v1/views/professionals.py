# -*- coding: utf-8 -*-
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.accounts.api.v1.serializers.professionals import ProfessionalSerializer
from apps.accounts.selectors.professionals import ProfessionalSelector
from apps.contrib.api.viewsets import PermissionViewSet


class ProfessionalsViewSet(PermissionViewSet):
    permission_classes = [IsAuthenticated]
    permissions_by_action = {
        'list': [AllowAny],
    }

    def list(self, request, **kwargs):
        professionals = ProfessionalSelector.get_active_professionals()
        return Response(ProfessionalSerializer(professionals, many=True).data)

    def appointments(self, request, **kwargs):
        """It shows the appointments to the professionals."""
        return Response({'status': 'OK'})

    def retrieve(self, request, **kwargs):
        return Response({'status': 'OK'})

    def calendar(self, request, **kwargs):
        return Response({'status': 'OK'})
