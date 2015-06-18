__author__ = 'nikosgpet'
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import StagesPlugin
from django.utils.translation import ugettext as _


class CMSStepPlugin(CMSPluginBase):
    model = StagesPlugin  # model where plugin data are saved
    module = "Step"
    name = _("Step Plugins") # name of the plugin in the interface
    render_template = "site_ied_plugins/steps_plugins.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        print "coucou"
        return context



plugin_pool.register_plugin(CMSStepPlugin)  # register the plugin