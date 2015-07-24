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
class Etape(models.Model):
    cod_etp = models.CharField('Code etp', max_length=15)
    label = models.CharField('label', max_length=120, null=True)

    @property
    def etape(self):
        if not hasattr(self, '_etape'):
            self._etape = SettingsEtape.objects.using('duck_duck').get(cod_etp=self.cod_etp)
        return self._etape

    @property
    def date_ouverture_equivalence(self):
        return self.etape.date_ouverture_equivalence

    @property
    def date_fermeture_equivalence(self):
        return self.etape.date_fermeture_equivalence

    @property
    def date_ouverture_candidature(self):
        return self.etape.date_ouverture_candidature

    @property
    def date_fermeture_candidature(self):
        return self.etape.date_fermeture_candidature

    @property
    def date_ouverture_inscription(self):
        return self.etape.date_ouverture_inscription

    @property
    def date_fermeture_inscription(self):
        return self.etape.date_fermeture_inscription

    @property
    def droit(self):
        return self.etape.droit

    @property
    def demi_tarif(self):
        return self.etape.demi_tarif

    @property
    def frais(self):
        return self.etape.frais

    @property
    def tarif_reins(self):
        """

        :return: frais de réins : frais si demi_tarif = false sinon frais/2
        """
        try:
            tarif = self.frais if not self.demi_tarif else self.frais/2
        except:
            tarif = None
        return tarif

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class StagesPlugin(CMSPlugin):
    stages = models.ManyToManyField(Etape)
    columns = models.CharField(choices=COLUMNS, max_length=30)
    template = models.CharField(choices=TEMPLATES, max_length=30)

    def __str__(self):
        return ' '.join(stage.label for stage in self.stages.all())

    def copy_relations(self, old_instance):
        self.stages = old_instance.stages.all()
        self.columns = old_instance.columns
        self.template = old_instance.template
        self.save()

