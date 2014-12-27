# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0003_auto_20141226_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertypicture',
            options={'ordering': ['index']},
        ),
        migrations.AddField(
            model_name='property',
            name='edit_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
