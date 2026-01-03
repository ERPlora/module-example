from django.apps import AppConfig


class ExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'example'
    verbose_name = 'Example Module'

    def ready(self):
        """Code executed when the module is loaded."""
        pass
