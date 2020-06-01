# -*- coding: utf-8 -*-

from django.urls import path

from apps.agendas.api.v1.views.appointments import AppointmentsViewSet
from apps.agendas.api.v1.views.patients import PatientsViewSet
from apps.agendas.api.v1.views.doctors import DoctorsViewSet


app_name = 'agendas'


urlpatterns = [

    # >> For Visitors
    path(
        'doctors/',
        DoctorsViewSet.as_view({'get': 'list'}),
        name='professionals',
    ),

    path(
        'me/appointments/',
        PatientsViewSet.as_view({'get': 'appointments'}),
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
            'delete': 'cancel',
        }),
        name='appointment',
    ),

    # >> For Professionals
    path(
        'doctors/<uuid:doctor_uuid>/',
        DoctorsViewSet.as_view({'get': 'retrieve'}),
        name='doctor',
    ),
    path(
        'doctors/<uuid:doctor_uuid>/appointments/',
        DoctorsViewSet.as_view({'get': 'appointments'}),
        name='professional-appointments',
    ),
    path(
        'doctors/<uuid:doctor_uuid>/calendar/',
        DoctorsViewSet.as_view({'get': 'calendar'}),
        name='doctor-calendar',
    ),


]
