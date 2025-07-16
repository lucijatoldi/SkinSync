from django.apps import AppConfig


class SkindiseaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skindisease'

    def ready(self):
        import skindisease.signals 
