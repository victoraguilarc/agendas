# -*- coding: utf-8 -*-

from apps.contrib.email import BaseEmailMessage


class ConfirmEmailMessage(BaseEmailMessage):
    """Email confirmation template."""

    subject = 'views/emails/confirm_email/subject.txt'
    message_text = 'views/emails/confirm_email/message.txt'
    message_html = 'views/emails/confirm_email/message.html'


class ResetPasswordMessage(BaseEmailMessage):
    """Reset password email template."""

    subject = 'views/emails/reset_password/subject.txt'
    message_text = 'views/emails/reset_password/message.txt'
    message_html = 'views/emails/reset_password/message.html'
