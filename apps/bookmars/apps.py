from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BookmarsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.bookmars"
    verbose_name = _("Bookmars")
