# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=255)),
                ('file_reference', models.CharField(max_length=255)),
                ('date', models.DateField(null=True)),
                ('court', models.CharField(max_length=255)),
                ('jurisdiction', models.CharField(max_length=255)),
                ('granted', models.CharField(max_length=25, choices=[(b'JA', b'Ja'), (b'NEIN', b'Nein'), (b'TEIL', b'Teilweise')])),
                ('value', models.DecimalField(null=True, max_digits=19, decimal_places=2)),
                ('value_currency', models.CharField(max_length=3)),
                ('link', models.CharField(max_length=255, blank=True)),
                ('subject', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('filename', models.CharField(max_length=255, blank=True)),
                ('text', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
