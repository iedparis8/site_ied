# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listview', '0002_auto_20150917_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listview',
            name='btn_more_link',
            field=models.CharField(default=b'', help_text=b'Lien du button', max_length=2048),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listview',
            name='btn_more_text',
            field=models.CharField(default=b'Texte du button', max_length=255),
            preserve_default=True,
        ),
    ]
