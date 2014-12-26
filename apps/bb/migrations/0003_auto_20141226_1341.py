# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0002_property_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertypicture',
            name='index',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(default=b'', max_length=250, editable=False),
        ),
    ]
