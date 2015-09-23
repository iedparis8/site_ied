from django.db import models
from cms.models import CMSPlugin
from listview.utils import get_personnel_member


class ListViewGroup(CMSPlugin):
    """
    A plugin that has ListView classes as children
    """
    def __unicode__(self):
        return u"{0} lists".format(self.cmsplugin_set.all().count())


class ListView(CMSPlugin):
    """
    A list of ListView Items, such as contact information, links etc...
    It has ListViewItem classes as children
    """
    title = models.CharField(max_length=64, default='')
    btn_more_text = models.CharField(max_length=255, blank='True', verbose_name='Texte du button Plus', )
    btn_more_link = models.CharField(max_length=2048, blank='True', verbose_name='Lien du button Plus')

    def __unicode__(self):
        return u"{0}".format(self.title)


class ListViewContactItem(CMSPlugin):
    """
    An individual ListView item for the ListView plugin
    """
    person = models.CharField(max_length=255, default='')
    color = models.CharField(max_length=255, default='orange')

    def __unicode__(self):
        p = get_personnel_member(int(self.person))
        return u"{0} {1}".format(p['prenom'], p['nom'])