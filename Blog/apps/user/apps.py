from django.apps import AppConfig

from apps import user


class UserConfig(AppConfig):
    name = 'apps.user'

    def ready(self):
        import apps.user.signals
