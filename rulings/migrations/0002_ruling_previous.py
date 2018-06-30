# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rulings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruling',
            name='previous',
            field=models.ForeignKey(related_name='next', to='rulings.Ruling', null=True, on_delete=models.SET_NULL),
            preserve_default=True,
        ),
    ]
