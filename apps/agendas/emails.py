# -*- coding: utf-8 -*-

from apps.contrib.email import BaseEmailMessage


class AppointmentEmailMessage(BaseEmailMessage):
    """Email confirmation template."""

    subject = 'transactions/emails/appointment/subject.txt'
    message_text = 'transactions/emails/appointment/message.txt'
    message_html = 'transactions/emails/appointment/message.html'
