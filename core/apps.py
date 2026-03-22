from django.apps import AppConfig
import os

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # Prevent double run
        if os.environ.get('RUN_MAIN') != 'true':
            return

        from .scheduler import start
        start()