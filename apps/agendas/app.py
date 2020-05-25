# -*- coding: utf-8 -*-

from django.apps import AppConfig


class AgendasConfig(AppConfig):
    """Configuration for project utilities."""

    name = 'apps.agendas'
    verbose_name = 'Agendas'

    def ready(self):
        """Override this to put in.
        """
