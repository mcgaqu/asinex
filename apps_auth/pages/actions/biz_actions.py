# -*- coding: utf-8 -*-
import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_auth.layouts.models import Layout




def ac_create_i18n(modeladmin, request, queryset):
    """
        1. Ejecutar la función definida en cada registro 
    """
    count = 0
    for obj in queryset:
        # import pdb; pdb.set_trace()
        if not obj.locked and obj.replace:
        # if obj.replace:
            obj.create_i18n()
        else:
            continue
            # message = _("el id:%s, %s no se carga porque está bloqueado") % (obj.id, obj.name)
    message = "Traducciones generadas: %s" % count
    modeladmin.message_user(request, message, level=messages.SUCCESS)
    return
ac_create_i18n.short_description = "Generar Traducciones"
