# -*- coding: utf-8 -*-

"""Production settings.

This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
https://docs.djangoproject.com/en/2.2/howto/deployment/
"""


from config.settings.components import env
from config.settings.components.common import TEMPLATES

DEBUG = False

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
SECRET_KEY = env('DJANGO_SECRET_KEY')

#
# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa: F405
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
     ),
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.MinimumLengthValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.CommonPasswordValidator'.format(_PASS),
    },
    {
        'NAME': '{0}.NumericPasswordValidator'.format(_PASS),
    },
]

# Security
# https://docs.djangoproject.com/en/2.2/topics/security/

# SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'
# STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'

