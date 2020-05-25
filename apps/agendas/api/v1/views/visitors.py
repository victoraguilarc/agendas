# -*- coding: utf-8 -*-


from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class VisitorsViewSet(ViewSet):
    """Process a google token_id login."""

    def appointments(self, request, **kwargs):
        """It shows the appointments to the customers."""
        return Response({'status': 'OK'})
