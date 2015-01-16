# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('temporary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporary',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_temporary.temporary_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
