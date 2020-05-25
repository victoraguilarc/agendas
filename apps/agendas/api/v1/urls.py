# -*- coding: utf-8 -*-

from django.urls import path

from apps.agendas.api.v1.views.appointments import AppointmentsViewSet
from apps.agendas.api.v1.views.visitors import VisitorsViewSet
from apps.agendas.api.v1.views.professionals import ProfessionalsViewSet

app_name = 'agendas'


urlpatterns = [

    # >> For Visitors
    path(
        'professionals/',
        ProfessionalsViewSet.as_view({'get': 'list'}),
        name='professionals',
    ),

    path(
        'me/appointments/',
        VisitorsViewSet.as_view({'get': 'appointments'}),
        name='scheduled-appointments',
    ),

    path(
        'appointments/',
        AppointmentsViewSet.as_view({'post': 'create'}),
        name='appointments',
    ),
    path(
        'appointments/<uuid:appointment_uuid>/',
        AppointmentsViewSet.as_view({
            'get': 'retrieve',
            'delete': 'destroy',
        }),
        name='appointment',
    ),

    # >> For Professionals
    path(
        'professionals/<uuid:professional_uuid>/',
        ProfessionalsViewSet.as_view({'get': 'retrieve'}),
        name='professional',
    ),
    path(
        'professionals/<uuid:professional_uuid>/appointments/',
        ProfessionalsViewSet.as_view({'get': 'appointments'}),
        name='professional-appointments',
    ),
    path(
        'professionals/<uuid:professional_uuid>/calendar/',
        ProfessionalsViewSet.as_view({'get': 'calendar'}),
        name='professional-appointments',
    ),


]
