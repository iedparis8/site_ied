# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listview', '0003_auto_20150917_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listview',
            name='btn_more_link',
        ),
        migrations.RemoveField(
            model_name='listview',
            name='btn_more_text',
        ),
        migrations.AddField(
            model_name='listview',
            name='Lien du button',
            field=models.CharField(default=b'', max_length=2048),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listview',
            name='Texte du button',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
