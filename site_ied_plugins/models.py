# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from cms.models import CMSPlugin
from duck_inscription.models.wish_models import SettingsEtape

COLUMNS = (
    ('toutes_dates', 'Toutes les dates'),
    ('equivalence', 'Dates Équivalence'),
    ('candidature', 'Dates Candidature'),
    ('inscription', 'Dates Inscription'),
    ('tarifs', 'Tarifs'),
)

TEMPLATES = (
    ('horizontal', 'Horizontal'),
    ('vertical', 'Vertical'),
)

@python_2_unicode_compatible
class StagesPlugin(CMSPlugin):
    stages = models.ManyToManyField(SettingsEtape)
    columns = models.CharField(choices=COLUMNS, max_length=30)
    template = models.CharField(choices=TEMPLATES, max_length=30)

    def __str__(self):
        return ' '.join(stage.label for stage in self.stages.all())

    def copy_relations(self, old_instance):
        self.stages = old_instance.stages.all()
        self.columns = old_instance.columns
        self.template = old_instance.template
        self.save()

