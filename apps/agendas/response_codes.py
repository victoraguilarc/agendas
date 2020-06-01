# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

DOCTOR_NOT_FOUND = {
    'code': 'agendas.DoctorNotFound',
    'detail': _('Doctor not Found'),
}

APPOINTMENT_NOT_FOUND = {
    'code': 'agendas.AppointmentNotFound',
    'detail': _('Appointment not Found'),
}

UNAVAILABLE_DATETIME = {
    'code': 'agendas.ReservedDateTime',
    'detail': _('This date and time was reserved'),
}
