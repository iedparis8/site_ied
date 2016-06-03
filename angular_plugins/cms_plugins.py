__author__ = 'nikosgpet'

from cms.plugin_base import CMSPluginBase
from angular_plugins.models import Angular
from cms.plugin_pool import plugin_pool


class AngularPlugin(CMSPluginBase):
    model = Angular
    name = "Angular Plugin"
    render_template = "angular_plugins/angular2.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(AngularPlugin)