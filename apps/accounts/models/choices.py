# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from apps.contrib.models.enums import BaseEnum
from apps.contrib.utils.choices import ListableStrPropsMixin


class Platform(BaseEnum):
    """Platform options for Phone Devices."""

    ANDROID = 'android'
    IOS = 'ios'
    WEB = 'web'

    @classmethod
    def choices(cls):  # noqa: D102
        return (
            (cls.ANDROID.value, _('Android')),
            (cls.IOS.value, _('iOS')),
            (cls.WEB.value, _('Web')),
        )


class ActionCategory(BaseEnum):
    """Action options for User actions."""

    CONFIRM_EMAIL = 'confirm_email'
    RESET_PASSWORD = 'reset_password'   # noqa: S105

    @classmethod
    def choices(cls):  # noqa: D102
        return (
            (cls.CONFIRM_EMAIL.value, _('Confirm e-mail')),
            (cls.RESET_PASSWORD.value, _('Reset Password')),
        )


class Specialties(ListableStrPropsMixin):
    """Contains all role vehicle commands."""

    PEDIATRICIAN = 'pediatrician'
    GENERAL_DOCTOR = 'general_doctor'

    @classmethod
    def choices(cls):
        return (
            (cls.PEDIATRICIAN, _('PEDIATRICIAN')),
            (cls.GENERAL_DOCTOR, _('GENERAL DOCTOR')),
        )
