import os

from django.apps import AppConfig
from django.db.models.signals import pre_save


class DoreadyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "doready"

    def ready(self):
        if not os.path.exists('module/output_type'):
            os.makedirs('module/output_type')
        if not os.path.exists('module/input_type'):
            os.makedirs('module/input_type')

        print("PicSmart is starting...")
        print("PicSmart is running...")
