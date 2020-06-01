import json

from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.agendas.selectors.appointment import AppointmentSelector


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        context['appointments'] = AppointmentSelector.user_appointments(self.request.user)
        return context
