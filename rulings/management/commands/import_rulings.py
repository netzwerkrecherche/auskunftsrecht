import json
import sys

from django.core.management.base import BaseCommand
from django.utils import translation
from django.conf import settings

from rulings.models import Ruling


class Command(BaseCommand):
    help = "Import JSON: python manage.py import_ruling [filename|stdin]"

    def handle(self, *args, **options):
        translation.activate(settings.LANGUAGE_CODE)
        if len(args) > 0:
            json_file = open(args[0])
        else:
            json_file = sys.stdin
        for row in json.load(json_file):
            ruling = None
            try:
                ruling = Ruling.objects.get(
                    file_reference=row['Aktenzeichen']
                )
            except Ruling.DoesNotExist:
                pass
            Ruling.objects.create_from_row(row, ruling=ruling)
