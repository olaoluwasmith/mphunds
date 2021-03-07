from django.apps import AppConfig


class MphundsappConfig(AppConfig):
    name = 'mphundsapp'

    def ready(self):
        import mphundsapp.signals
