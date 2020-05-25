# -*- coding: utf-8 -*-

from apps.accounts.models import UserProfile

from django.contrib import admin


@admin.register(UserProfile)
class UserProfiledmin(admin.ModelAdmin):
    """Defines the phone device admin behaviour."""

    list_display = ('specialty', 'user')
    search_fields = ('user__email', 'user__username')
    raw_id_fields = ('user', )
