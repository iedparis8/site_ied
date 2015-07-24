# coding=utf-8
from __future__ import unicode_literals
from cms.models import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class AnneeUni(models.Model):
    """Class d'accès pour la modification

    """
    cod_anu = models.CharField(u'Année', max_length=4, primary_key=True, db_column='COD_ANU')
    eta_anu_iae = models.CharField(u"Etat ouverture année", max_length=1, choices=(
        ('F', u"Fermé"),
        ('I', 'Inscription'),
        ('O', 'Ouvert')), default='I', db_column='ETA_ANU_IAE')

    def __str__(self):
        return str(self.cod_anu)

    class Meta:
        managed = False
        db_table = 'ANNEE_UNI'
        ordering = ['-cod_anu']


@python_2_unicode_compatible
class Etape(models.Model):
    cod_etp = models.CharField(u"Code etape", max_length=6, db_column="COD_ETP", primary_key=True, )
    cod_cyc = models.CharField(u"code sise", max_length=1, null=True, db_column="COD_CYC")
    cod_cur = models.CharField(u"cursus lmd", max_length=1, null=True, db_column="COD_CUR")
    lib_etp = models.CharField(u"label", max_length=60, null=True, db_column="LIB_ETP")

    def __str__(self):
        return u"%s" % self.lib_etp

    class Meta:
        managed = False
        verbose_name = "Etape d'un cursus"
        verbose_name_plural = "Etapes d'un cursus"
        db_table = "ETAPE"


@python_2_unicode_compatible
class SettingAnneeUni(AnneeUni):
    inscription = models.BooleanField(default=False)
    transfert_pdf = models.FileField(upload_to='document_inscription', null=True, blank=True)
    bourse_pdf = models.FileField(upload_to='document_inscription', null=True, blank=True)
    pieces_pdf = models.FileField(upload_to='document_inscription', null=True, blank=True)
    tarif_medical = models.FloatField('tarif medical', null=True, blank=True)
    tarif_secu = models.FloatField('tarif secu', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'duck_inscription_settinganneeuni'
        verbose_name = 'Setting année universitaire'
        verbose_name_plural = u'Settings année universitaire'

    def __str__(self):
        if self.inscription:
            inscription = 'inscription ouverte'
        else:
            inscription = 'inscription fermée'
        return '{} {}'.format(self.cod_anu, inscription)


@python_2_unicode_compatible
class SettingsEtape(Etape):
    label = models.CharField('Label', max_length=120, null=True)
    diplome = models.ForeignKey('DiplomeEtape', null=True, blank=True)
    cursus = models.ForeignKey('CursusEtape', null=True, blank=True)
    required_equivalence = models.BooleanField('Equivalence obligatoire', default=True)
    is_inscription_ouverte = models.BooleanField('ouverture campagne inscription', default=True)
    date_ouverture_equivalence = models.DateTimeField(null=True, blank=True)
    date_fermeture_equivalence = models.DateTimeField(null=True, blank=True)
    date_ouverture_candidature = models.DateTimeField(null=True, blank=True)
    date_fermeture_candidature = models.DateTimeField(null=True, blank=True)
    date_ouverture_inscription = models.DateTimeField(null=True, blank=True)
    date_fermeture_inscription = models.DateTimeField(null=True, blank=True)
    date_fermeture_reinscription = models.DateTimeField(null=True, blank=True)

    label_formation = models.CharField(max_length=120, null=True, blank=True)
    annee = models.ForeignKey(SettingAnneeUni, default=2014)
    autres = models.FileField(upload_to='document_autre', null=True, blank=True)
    document_equivalence = models.FileField(upload_to='document_equivalence',
                                            verbose_name=u"Document d'équivalence", null=True, blank=True)
    document_candidature = models.FileField(upload_to='document_candidature',
                                            verbose_name=u"Document de candidature", null=True, blank=True)
    note_maste = models.BooleanField(default=False)
    path_template_equivalence = models.CharField('Path Template Equivalence', max_length=1000, null=True, blank=True)
    grille_de_equivalence = models.FileField(upload_to='grilles_evaluations', null=True, blank=True,
                                             verbose_name="Grille evaluations")

    droit = models.FloatField(u"Droit", default=186)
    frais = models.FloatField(u"Frais", default=1596)
    nb_paiement = models.IntegerField(u"Nombre paiement", default=3)
    demi_tarif = models.BooleanField(u"Demi tarif en cas de réins", default=False)
    semestre = models.BooleanField(u"Demie année", default=False)

    limite_etu = models.IntegerField(u"Capacité d'accueil", null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'duck_inscription_settingsetape'
        verbose_name = 'Settings Etape'
        verbose_name_plural = 'Settings Etapes'

    def can_demi_annee(self, reins):
        if self.semestre and not reins:
            return True
        return False

    def tarif_reins(self):
        """

        :return: frais de réins : frais si demi_tarif = false sinon frais/2
        """
        try:
            tarif = self.frais if not self.demi_tarif else self.frais/2
        except:
            tarif = None
        return tarif

    def get_tarif_paiement(self, reins=False, semestre=False):
        tarif = self.frais
        if self.demi_tarif and (reins or semestre):
            tarif /= 2
        return tarif

    def __str__(self):
        result = self.label or ""
        return result


@python_2_unicode_compatible
class DiplomeEtape(models.Model):
    label = models.CharField('Label web', max_length=120, null=True)
    is_inscription_ouverte = models.BooleanField('ouverture campagne inscription', default=True)

    class Meta:
        managed = False
        db_table = 'duck_inscription_diplomeetape'
        verbose_name_plural = 'Diplomes'
        verbose_name = 'Diplômes'

    def __str__(self):
        return self.label or ''


@python_2_unicode_compatible
class CursusEtape(models.Model):
    label = models.CharField('Label web', max_length=200, null=True)

    class Meta:
        db_table = 'duck_inscription_cursusetape'
        managed = False
        verbose_name_plural = 'Cursus'
        verbose_name = 'Cursus'

    def __str__(self):
        return self.label or ''


@python_2_unicode_compatible
class CentreGestionModel(models.Model):
    centre_gestion = models.CharField('', max_length=3)
    label = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'duck_inscription_centregestionmodel'
        verbose_name = u"Centre de gestion"
        verbose_name_plural = u"Centres de gestion"

    def __str__(self):
        return unicode(self.label)


