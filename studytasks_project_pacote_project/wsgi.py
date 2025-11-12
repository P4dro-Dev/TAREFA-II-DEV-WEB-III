"""
WSGI project for studytasks_project_pacote project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studytasks_project_pacote_project.settings')

application = get_wsgi_application()
