import os

from celery import Celery
from django.conf import settings

#TODO: change this in production

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_blog_api.settings.develop")

app = Celery("tech_blog_api")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)