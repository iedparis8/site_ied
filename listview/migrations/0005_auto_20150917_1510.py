# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listview', '0004_auto_20150917_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listview',
            name='Lien du button',
        ),
        migrations.RemoveField(
            model_name='listview',
            name='Texte du button',
        ),
        migrations.AddField(
            model_name='listview',
            name='btn_more_link',
            field=models.CharField(default=b'', max_length=2048, verbose_name=b'Lien du button Plus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listview',
            name='btn_more_text',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Texte du button Plus'),
            preserve_default=True,
        ),
    ]
