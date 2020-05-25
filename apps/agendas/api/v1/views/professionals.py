# -*- coding: utf-8 -*-


from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class ProfessionalsViewSet(ViewSet):
    """Process a google token_id login."""

    def list(self, request, **kwargs):
        return Response({'status': 'OK'})

    def appointments(self, request, **kwargs):
        """It shows the appointments to the professionals."""
        return Response({'status': 'OK'})

    def retrieve(self, request, **kwargs):
        return Response({'status': 'OK'})

    def calendar(self, request, **kwargs):
        return Response({'status': 'OK'})
