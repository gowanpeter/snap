# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='documentation_name',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='exhibitionlookup',
            name='exhibition_name',
            field=models.CharField(max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='catalogue_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='piece',
            name='cataloguer',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='heath_id',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='piece_description',
            field=models.CharField(max_length=22, blank=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='piece_name',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AlterField(
            model_name='publicationlookup',
            name='publication_name',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='setcollection',
            name='set_collection_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
