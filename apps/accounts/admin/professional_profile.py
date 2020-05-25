# -*- coding: utf-8 -*-

from apps.accounts.models import ProfessionalProfile

from django.contrib import admin


@admin.register(ProfessionalProfile)
class ProfessionalProfiledmin(admin.ModelAdmin):
    """Defines the phone device admin behaviour."""

    list_display = ('specialty', 'user', 'verified')
    search_fields = ('user__email', 'user__username')
    raw_id_fields = ('user', )
    list_filter = ('specialty', 'location', 'verified')
