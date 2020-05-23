from django.core.management.base import BaseCommand
from covidregister.register.models import Patient


class Command(BaseCommand):
    def handle(self, *args, **options):
        Patient.objects.all().delete()
