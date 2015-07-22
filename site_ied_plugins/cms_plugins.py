# -*- coding: utf-8 -*-
__author__ = 'nikosgpet'

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import StagesPlugin
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin
class CMSStepPlugin(CMSPluginBase):
    model = StagesPlugin  # model where plugin data are saved
    module = "Step"
    name = _("Step Plugins") # name of the plugin in the interface
    render_template = "site_ied_plugins/steps_plugins.html"

    def render(self, context, instance, placeholder):

        # Does any of the steps have a demi tarif?
        demi_tarif = False
        for step in instance.stages.all():
            if step.demi_tarif:
                demi_tarif = True

        # Does any of the steps have dates for candidature?
        candidature = False
        for step in instance.stages.all():
            if step.date_ouverture_candidature or step.date_fermeture_candidature:
                candidature = True

        # For every step, add the suitable title in row[0] and the suitable contents in the rows that follow
        col = instance.columns
        rows = []
        for i, step in enumerate(instance.stages.all()):
            if i == 0:
                rows.append(['Diplome'])
            rows.append([step.label])

            if col == 'toutes_dates' or col == 'equivalence':
                if i == 0:
                    rows[i] += ['Ouverture equivalence', 'Fermeture equivalence']
                rows[i+1] += [step.date_ouverture_equivalence, step.date_fermeture_equivalence]
            if candidature and (col == 'toutes_dates' or col == 'candidature'):
                if i == 0:
                    rows[i] += ['Ouverture candidature', 'Fermeture candidature']
                rows[i+1] += [step.date_ouverture_candidature, step.date_fermeture_candidature]
            if col == 'toutes_dates' or col == 'inscription':
                if i == 0:
                    rows[i] += ['Ouverture inscription', 'Fermeture inscription']
                rows[i+1] += [step.date_ouverture_inscription, step.date_fermeture_inscription]
            if instance.columns == 'tarifs':
                if i == 0:
                    rows[i] += ['Droits universitaires', "Frais propres à l'enseignement à distance"]
                rows[i+1] += [step.droit, step.frais]
                # Only add the demi tarifs column, if it exists
                if demi_tarif:
                    if i == 0:
                        rows[i] += ["Frais propres à l'enseignement à distance en réinscription"]
                    rows[i+1] += [step.tarif_reins]

        if instance.template == 'vertical':
            rows = zip(*rows)

        context.update({'instance': instance, 'rows': rows})
        return context
