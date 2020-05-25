# -*- coding: utf-8 -*-

from rest_framework import serializers
from apps.accounts.models import ProfessionalProfile


class ProfessionalSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = ProfessionalProfile
        fields = (
            'uuid',
            'email',
            'first_name',
            'last_name',
            'specialty',
            'title',
            'location',
            'verified',
        )
        read_only_fields = fields
