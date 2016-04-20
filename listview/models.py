from django.db import models
from cms.models import CMSPlugin
from listview.utils import get_personnel_member
from cms.models.fields import PageField
from django.conf import settings


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
    btn_more_text = models.CharField(max_length=255, blank='True', verbose_name='texte',
                                     help_text='Texte du button "Plus"')
    btn_more_link = models.CharField(max_length=2048, blank='True', verbose_name='lien',
                                     help_text='Lien du button "Plus"')
    page_link = PageField(verbose_name="page", blank=True, null=True,
                          help_text="Une page a plus du priorite qu'un lien")

    def __unicode__(self):
        return u"{0}".format(self.title)


class ListViewContactItem(CMSPlugin):
    """
    An individual ListView item for the ListView plugin
    """
    person = models.CharField(max_length=255, default='')
    color = models.CharField(max_length=255, choices=settings.COLOR_CHOICES, default=None,
                             verbose_name='couleur')

    def __unicode__(self):
        p = get_personnel_member(int(self.person))
        return u"{0} {1}".format(p['prenom'], p['nom'])


class ListViewLinkItem(CMSPlugin):
    """
    An individual ListView item for the ListView plugin
    """
    title = models.CharField('titre', max_length=255)
    subtitle = models.CharField('sous-titre', max_length=255)
    url = models.CharField("url", blank=True, null=True, max_length=255)
    page_link = PageField(verbose_name="page", blank=True, null=True,
                          help_text="Une page a plus du priorite qu'un lien")
    new_window = models.BooleanField("new window?", default=False,
                                     help_text="Tu veux que le lien ouvre dans une nouvelle fenetre?")
    color = models.CharField(max_length=255, default=None, choices=settings.COLOR_CHOICES, blank=True,
                             verbose_name='couleur')

    def __unicode__(self):
        return u"{0}".format(self.title)
