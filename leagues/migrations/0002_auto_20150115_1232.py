# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporary', '0002_temporary_polymorphic_ctype'),
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='id',
        ),
        migrations.AddField(
            model_name='league',
            name='temporary_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='temporary.Temporary'),
            preserve_default=False,
        ),
    ]
