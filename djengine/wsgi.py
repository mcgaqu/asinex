"""
WSGI config for djengine project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from .settings import WSITE_NAME
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % WSITE_NAME)


application = get_wsgi_application()
