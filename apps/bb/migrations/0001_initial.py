# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('cell', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('div_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('cell', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Municipalities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('bedrooms', models.PositiveSmallIntegerField(default=1)),
                ('bath_rooms', models.PositiveSmallIntegerField(default=1)),
                ('description', models.TextField()),
                ('rate_per_room', models.DecimalField(max_digits=6, decimal_places=2)),
                ('near_by_places', models.TextField(default=b'', blank=True)),
                ('active', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(to='bb.Contact')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facility', models.ForeignKey(to='bb.Facility')),
                ('property', models.ForeignKey(related_name=b'amenities', to='bb.Property')),
            ],
            options={
                'verbose_name': 'Property Facility',
                'verbose_name_plural': 'Property Facilities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'/Users/edilio/projects/cubabnb/media/images')),
                ('tag', models.CharField(max_length=30, null=True, blank=True)),
                ('property', models.ForeignKey(to='bb.Property')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewGuide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.PositiveSmallIntegerField(choices=[(0, b'0 - Stars'), (1, b'1 - Stars'), (2, b'2 - Stars'), (3, b'3 - Stars'), (4, b'4 - Stars'), (5, b'5 - Stars')])),
                ('note', models.TextField()),
                ('nick_name', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('guide', models.ForeignKey(to='bb.Guide')),
            ],
            options={
                'verbose_name': 'Review Guide',
                'verbose_name_plural': 'Review Guides',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.PositiveSmallIntegerField(choices=[(0, b'0 - Stars'), (1, b'1 - Stars'), (2, b'2 - Stars'), (3, b'3 - Stars'), (4, b'4 - Stars'), (5, b'5 - Stars')])),
                ('note', models.TextField()),
                ('nick_name', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('property', models.ForeignKey(to='bb.Property')),
            ],
            options={
                'verbose_name': 'Review Property',
                'verbose_name_plural': 'Review Properties',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='municipality',
            name='province',
            field=models.ForeignKey(to='bb.Province'),
            preserve_default=True,
        ),
    ]
