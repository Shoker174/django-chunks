# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chunk',
            options={'verbose_name': 'Chunk', 'verbose_name_plural': 'Chunks'},
        ),
        migrations.AlterField(
            model_name='chunk',
            name='content',
            field=models.TextField(verbose_name='Content', blank=True),
        ),
        migrations.AlterField(
            model_name='chunk',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='chunk',
            name='key',
            field=models.CharField(help_text='A unique name for this chunk of content', unique=True, max_length=255, verbose_name='Key'),
        ),
    ]
