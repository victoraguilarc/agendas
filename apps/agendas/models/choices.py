# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from apps.contrib.utils.choices import ListableStrPropsMixin


class AppointmentStatus(ListableStrPropsMixin):
    REQUESTED = 'REQUESTED'
    ACCEPTED = 'ACCEPTED'
    CANCELLED = 'CANCELLED'
    DENIED = 'DENIED'

    @classmethod
    def choices(cls):
        return (
            (cls.REQUESTED, _('REQUESTED')),
            (cls.ACCEPTED, _('ACCEPTED')),
            (cls.CANCELLED, _('CANCELLED')),
            (cls.DENIED, _('DENIED')),
        )


class AppointmentSite(ListableStrPropsMixin):
    IN_PLACE = 'IN_PLACE'
    ONLINE = 'ONLINE'

    @classmethod
    def choices(cls):
        return (
            (cls.IN_PLACE, _('IN_PLACE')),
            (cls.ONLINE, _('ONLINE')),
        )
