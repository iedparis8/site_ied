import requests
from cms.plugin_base import CMSPluginBase
from listview.models import ListViewGroup, ListView, ListViewContactItem
from listview.forms import PersonnelForm
from cms.plugin_pool import plugin_pool
from listview.utils import get_personnel, get_personnel_member

class ListViewGroupPlugin(CMSPluginBase):
    model = ListViewGroup
    name = "List View Group"
    render_template = "listview/listview_group.html"
    allow_children = True
    child_classes = ["ListViewPlugin", "NewsBlogLatestArticlesPlugin", ]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ListViewPlugin(CMSPluginBase):
    model = ListView
    name = "List View"
    render_template = "listview/listview.html"
    parent_classes = ["ListViewGroupPlugin"]
    allow_children = True
    child_classes = ["ListViewContactItemPlugin", ]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ListViewContactItemPlugin(CMSPluginBase):
    model = ListViewContactItem
    name = "List View Contact"
    render_template = "listview/listview_contact.html"
    parent_classes = ["ListViewPlugin"]
    form = PersonnelForm

    def render(self, context, instance, placeholder):
        p = get_personnel_member(int(instance.person))
        phone = p['phone'][:2] + ' ' + p['phone'][2:] if p['phone'] else ""

        context.update({
            'instance': instance,
            'name': p['prenom'],
            'surname': p['nom'],
            'function': p['fonction_name_list'][0],
            'phone': phone,
            'email': p['email'],
        })
        return context

plugin_pool.register_plugin(ListViewGroupPlugin)
plugin_pool.register_plugin(ListViewPlugin)
plugin_pool.register_plugin(ListViewContactItemPlugin)
