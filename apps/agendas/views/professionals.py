import json

from django.views.generic import TemplateView, DetailView

from apps.agendas.models import DoctorProfile
from apps.agendas.selectors.professionals import DoctorSelector
from apps.agendas.services.professionals import DoctorService


class DoctorsView(TemplateView):
    template_name = 'professionals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['professionals'] = DoctorSelector.get_enabled_doctors()
        return context


class DoctorProfileAgendaView(DetailView):
    template_name = 'professional.html'
    model = DoctorProfile
    slug_field = 'uuid'
    slug_url_kwarg = 'professional_uuid'
    query_pk_and_slug = True
    context_object_name = 'professional'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['week'] = DoctorService.calendar(context['professional'])
        context['week_json'] = json.dumps(context['week'])
        week = DoctorService.get_week()
        context['week_number'] = week['week_number']
        context['year'] = week['year']
        return context


class DoctorProfileView(DetailView):
    template_name = 'visitor.html'
    model = DoctorProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
