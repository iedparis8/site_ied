# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duck_inscription', '0003_auto_20150619_1114'),
        ('cms', '0011_auto_20150419_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='StagesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('columns', models.CharField(max_length=30, choices=[('tout', 'Tout'), ('equivalence', '\xc9quivalence'), ('candidature', 'Candidature'), ('inscription', 'Inscription'), ('tarifs', 'Tarifs')])),
                ('template', models.CharField(max_length=30, choices=[('horizontal.html', 'Horizontal'), ('vertical.html', 'Vertical')])),
                ('stages', models.ManyToManyField(to='duck_inscription.SettingsEtape')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
