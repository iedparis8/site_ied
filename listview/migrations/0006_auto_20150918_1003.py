# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listview', '0005_auto_20150917_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listview',
            name='btn_more_link',
            field=models.CharField(max_length=2048, verbose_name=b'Lien du button Plus', blank=b'True'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listview',
            name='btn_more_text',
            field=models.CharField(max_length=255, verbose_name=b'Texte du button Plus', blank=b'True'),
            preserve_default=True,
        ),
    ]
