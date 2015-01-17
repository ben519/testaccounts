# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_key', models.CharField(max_length=40, editable=False)),
                ('ip_address', models.CharField(max_length=40, editable=False)),
                ('pub_date', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, db_index=True, editable=True, blank=True)),
                ('last_modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=True, blank=True)),
                ('user', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
