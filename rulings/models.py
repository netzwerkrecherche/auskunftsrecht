import decimal

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class RulingManager(models.Manager):
    MAPPING = {
        'Gericht': 'court',
        'Aktenzeichen': 'file_reference',
        'Ebene': 'jurisdiction',
        'Auskunft erteilt?': 'granted',
        'Verlinkung': 'link',
        'Gegenstand': 'subject',
        'Inhalt': 'content',
        'filename': 'filename',
        'text': 'text'
    }

    def create_from_row(self, row, ruling=None):
        if ruling is None:
            ruling = Ruling()
        for key, attr in self.MAPPING.items():
            setattr(ruling, attr, row[key])

        ruling.value_currency = 'EUR'
        value = row['Streitwert']
        value = value.strip()
        parts = value.split(' ', 1)
        if len(parts) > 1:
            ruling.value_currency = parts[1]

        value = parts[0]
        value = value.replace(',', '.')
        if value:
            ruling.value = decimal.Decimal(value)
        else:
            ruling.value = None
        ruling.slug = slugify(ruling.file_reference)

        link = row.get('Verlinkung', '').strip()
        if link:
            prev = Ruling.objects.get(file_reference=link)
            ruling.previous = prev

        ruling.save()
        return ruling


class Ruling(models.Model):
    GRANT_CHOICES = (
        ('JA', 'Ja'),
        ('NEIN', 'Nein'),
        ('TEIL', 'Teilweise'),
    )

    slug = models.SlugField(max_length=255)
    file_reference = models.CharField(max_length=255)
    date = models.DateField(null=True)
    court = models.CharField(max_length=255)
    jurisdiction = models.CharField(max_length=255)
    granted = models.CharField(max_length=25, choices=GRANT_CHOICES)
    value = models.DecimalField(null=True, decimal_places=2, max_digits=19)
    value_currency = models.CharField(max_length=3)
    link = models.CharField(max_length=255, blank=True)
    subject = models.TextField(blank=True)
    content = models.TextField(blank=True)
    filename = models.CharField(max_length=255, blank=True, default='')
    text = models.TextField(blank=True)
    previous = models.ForeignKey('self', null=True, related_name="next")

    objects = RulingManager()

    def __unicode__(self):
        return self.file_reference

    def get_absolute_url(self):
        return reverse('show_ruling', kwargs={'slug': self.slug})
