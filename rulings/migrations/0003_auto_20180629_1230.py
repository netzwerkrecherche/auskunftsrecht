# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rulings', '0002_ruling_previous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruling',
            name='filename',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
