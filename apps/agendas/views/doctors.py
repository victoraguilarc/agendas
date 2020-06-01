import json

from django.views.generic import TemplateView, DetailView

from apps.agendas.models import DoctorProfile
from apps.agendas.selectors.doctor_profile import DoctorProfileSelector
from apps.agendas.services.doctor_profile import DoctorProfileService


class DoctorsView(TemplateView):
    template_name = 'doctors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['doctors'] = DoctorProfileSelector.get_enabled_doctors()
        return context


class DoctorProfileAgendaView(DetailView):
    template_name = 'doctor.html'
    model = DoctorProfile
    slug_field = 'uuid'
    slug_url_kwarg = 'doctor_uuid'
    query_pk_and_slug = True
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['week'] = DoctorProfileService.week_calendar(context['doctor'])
        context['week_json'] = json.dumps(context['week'])
        week = DoctorProfileService.get_week()
        context['week_number'] = week['week_number']
        context['year'] = week['year']
        return context


class DoctorProfileView(DetailView):
    template_name = 'profile.html'
    model = DoctorProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
