import json

from django.core.management.base import BaseCommand
from django.utils import translation
from django.conf import settings

from rulings.models import Ruling


class Command(BaseCommand):
    help = "Import JSON"

    def handle(self, *args, **options):
        translation.activate(settings.LANGUAGE_CODE)

        filename = args[0]
        for row in json.load(file(filename)):
            ruling = None
            try:
                ruling = Ruling.objects.get(
                    file_reference=row['Aktenzeichen']
                )
            except Ruling.DoesNotExist:
                pass
            Ruling.objects.create_from_row(row, ruling=ruling)
