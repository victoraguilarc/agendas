# -*- coding: utf-8 -*-

from django.urls import path
from apps.agendas.views.doctors import DoctorsView, DoctorProfileAgendaView, DoctorProfileView
from apps.agendas.views.visitors import UserProfileView

app_name = 'agendas'
urlpatterns = [
    # > Transactions
    path(
        '',
        DoctorsView.as_view(),
        name='doctors',
    ),

    # >> Profiles
    path(
        'profile/',
        UserProfileView.as_view(),
        name='profile',
    ),

    path(
        'doctor/<uuid:doctor_uuid>/',
        view=DoctorProfileAgendaView.as_view(),
        name='doctor-agenda',
    )
]
