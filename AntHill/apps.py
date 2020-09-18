from django.apps import AppConfig


class AnthillConfig(AppConfig):
    name = 'AntHill'

    def ready(self):
    	import AntHill.signals

