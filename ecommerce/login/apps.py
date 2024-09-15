from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class LoginConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "login"

class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"