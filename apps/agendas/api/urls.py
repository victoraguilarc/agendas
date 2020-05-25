# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    path('v1/', include('apps.agendas.api.v1.urls', namespace='v1')),
]
