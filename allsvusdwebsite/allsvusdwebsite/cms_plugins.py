from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import QuickLinkCardInfo
from .models import EventCardInfo

@plugin_pool.register_plugin
class QuickLinkCardPlugin(CMSPluginBase):
    model = QuickLinkCardInfo
    name = _("Quick Link Card")
    render_template = "quick_link_card.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class EventCardPlugin(CMSPluginBase):
    model = EventCardInfo
    name = _("Event Card")
    render_template = "event_card.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context