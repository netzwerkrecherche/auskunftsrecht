import json
import csv
import subprocess
import os

from django.core.management.base import BaseCommand
from django.utils import translation
from django.conf import settings


class Command(BaseCommand):
    help = "Extract CSV: python manage.py extract_ruling <csv_file> <path>"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        translation.activate(settings.LANGUAGE_CODE)
        self.get_json(options['csv_file'], options['path'])

    def get_json(self, csv_file, path, out=None):
        if out is None:
            out = self.stdout

        reader = csv.DictReader(open(csv_file))
        all_urteile = []
        for urteil in reader:
            filename = '%s.pdf' % urteil['Aktenzeichen'].replace('/', '.')
            full_path = os.path.join(path, filename)
            if os.path.exists(full_path):
                text = self.get_content(full_path)
            else:
                filename = None
                text = None
            urteil['filename'] = filename
            urteil['text'] = text
            all_urteile.append(urteil)
        json.dump(all_urteile, out)

    def get_content(self, filename):
        text_file = filename.rsplit('.', 1)[0] + '.txt'
        if os.path.exists(text_file):
            return open(text_file).read()
        process = subprocess.Popen(['pdftotext', filename],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        if process.returncode != 0:
            return None
        with open(text_file) as f:
            text = f.read()
        return text
