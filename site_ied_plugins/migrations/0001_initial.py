# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod_etp', models.CharField(max_length=15, verbose_name='Code etp')),
                ('label', models.CharField(max_length=120, null=True, verbose_name='label')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StagesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('columns', models.CharField(max_length=30, choices=[('toutes_dates', 'Toutes les dates'), ('equivalence', 'Dates \xc9quivalence'), ('candidature', 'Dates Candidature'), ('inscription', 'Dates Inscription'), ('tarifs', 'Tarifs')])),
                ('template', models.CharField(max_length=30, choices=[('horizontal', 'Horizontal'), ('vertical', 'Vertical')])),
                ('stages', models.ManyToManyField(to='site_ied_plugins.Etape')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
