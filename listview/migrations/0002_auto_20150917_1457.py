# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listview',
            name='btn_more_link',
            field=models.CharField(default=b'', max_length=2048),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listview',
            name='btn_more_text',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
