# -*- coding: utf-8 -*-


from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class AppointmentsViewSet(ViewSet):
    """Process a google token_id login."""

    def create(self, request, **kwargs):
        return Response({'status': 'OK'})

    def retrieve(self, request, **kwargs):
        return Response({'status': 'OK'})

    def cancel(self, request, **kwargs):
        return Response({'status': 'OK'})

