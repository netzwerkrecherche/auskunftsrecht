import unicodecsv
import json
import subprocess
import os

from django.core.management.base import BaseCommand
from django.utils import translation
from django.conf import settings


class Command(BaseCommand):
    help = "Extract CSV: python manage.py extract_ruling <csv_file> <path>"

    def handle(self, *args, **options):
        translation.activate(settings.LANGUAGE_CODE)
        self.get_json(args[0], args[1])

    def get_json(self, csv_file, path, out=None):
        if out is None:
            out = self.stdout

        reader = unicodecsv.DictReader(open(csv_file), encoding='utf-8')
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
            return open(text_file).read().decode('utf-8')
        process = subprocess.Popen(['pdftotext', filename],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        if process.returncode != 0:
            return None
        with open(text_file) as f:
            text = f.read()
        return text.decode('utf-8')
