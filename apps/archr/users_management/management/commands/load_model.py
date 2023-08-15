from bark import preload_models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Add Sample Data"

    def handle(self, *args, **options):
        preload_models()
