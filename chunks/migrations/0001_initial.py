# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text=b'A unique name for this chunk of content', unique=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
