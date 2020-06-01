# -*- coding: utf-8 -*-

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse, path, re_path
from django.utils.html import format_html

from apps.agendas.admin.forms.appointment_reminder import AppointmentReminderForm
from apps.agendas.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'status',
        'date',
        'time',
        'appointment_actions',
    )
    raw_id_fields = ('doctor', 'visitor')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<uuid:appointment_uuid>/reminder/',
                self.admin_site.admin_view(self.process_reminder),
                name='appointment-reminder',
            ),
        ]
        return custom_urls + urls

    def process_reminder(self, request, account_id, *args, **kwargs):
        return self.process_action(
            request=request,
            account_id=account_id,
            action_form=AppointmentReminderForm,
            action_title='Deposit',
        )

    def process_action(self, request, account_id, action_form, action_title):
        account = self.get_object(request, account_id)
        if request.method != 'POST':
            form = action_form()
        else:
            form = action_form(request.POST)
            if form.is_valid():
                try:
                    form.save(account, request.user)
                except Exception as e:
                    # If save() raised, the form will a have a non
                    # field error containing an informative message.
                    pass
                else:
                    self.message_user(request, 'Success')
                    url = reverse(
                        'admin:account_account_change',
                        args=[account.pk],
                        current_app=self.admin_site.name,
                    )
                    return HttpResponseRedirect(url)

        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form
        context['account'] = account
        context['title'] = action_title
        return TemplateResponse(
            request,
            'admin/account/account_action.html',
            context,
        )

    def appointment_actions(self, appointment):
        return format_html(
            '<a class="button" href="{}">Send Reminder</a>&nbsp;',
            reverse('admin:appointment-reminder', args=[appointment.uuid]),
        )

    appointment_actions.short_description = 'Actions'
    appointment_actions.allow_tags = True

