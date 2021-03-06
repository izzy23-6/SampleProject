"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'source.settings')
# django.setup()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "source.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

