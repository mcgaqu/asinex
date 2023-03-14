import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import get_website
from ..models import Layout, Component


def load_layouts():
    get_DATA = getattr(
        import_module('%s.datainit' % settings.WSITE_NAME),
        'get_LAYOUTS_DATA')
    data = get_DATA()
    website = get_website()
    # import pdb; pdb.set_trace()
    if not data: return
    for row in data: # [root_alias,  get_LAYOUT_DATAx?, grade=languages,]
        try:
            ly_root = Layout.objects.get(website=website, pos="", root_alias=row[0], last_alias='', level=0)
        except Layout.DoesNotExist:
            ly_root = Layout(website=website, root_alias=row[0], sort="", last_alias="")
            ly_root.params = row[2]
            ly_root.save()
            # ly_root.expand_layout()
        if False:
            try:
                comp_root = Component.objects.get(website=website, pos="", root_alias=row[0], last_alias='', level=0)
            except Component.DoesNotExist:
                comp_root = Component(website=website, root_alias=row[0], sort="", last_alias="")
                # comp_root.params = row[2]
                comp_root.save()
    return








