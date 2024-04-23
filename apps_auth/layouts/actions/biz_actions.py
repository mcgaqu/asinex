# -*- coding: utf-8 -*-
import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_auth.layouts.models import Layout

def ac_expand_layout(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.parent and not obj.locked:
            obj.expand_layout()
            message = "Función expand_layout para %s realizada" % obj.root_alias
            modeladmin.message_user(request, message, level=messages.SUCCESS)
        else:
            message = _("el layout:%s, %s no se carga porque no es raiz o está bloqueado") % (obj.id, obj.name)
            modeladmin.message_user(request, message, level=messages.warning)
        return
ac_expand_layout.short_description = "Crear Layout con sus Componentes"



def ac_create_i18n(modeladmin, request, queryset):
    """
        1. Ejecutar la función definida en cada registro 
    """
    count = 0
    for obj in queryset:
        # import pdb; pdb.set_trace()
        # if not obj.locked and obj.replace:
        if obj.replace:
            try:
                root_obj = Layout.objects.get(wsite=obj.wsite, 
                    root_alias=obj.root_alias, level=0)
                languages = root_obj.name.split(',')
                obj.create_i18n(languages)
                count +=1
            except Layout.DoesNotExist:
                continue
        else:
            continue
            # message = _("el id:%s, %s no se carga porque está bloqueado") % (obj.id, obj.name)
    message = "Traducciones generadas: %s" % count
    modeladmin.message_user(request, message, level=messages.SUCCESS)
    return
ac_create_i18n.short_description = "Generar Traducciones"



def ac_expand_component_layout(modeladmin, request, queryset):
    """
        1. Ejecutar la función definida en cada registro 
    """

    for obj in queryset:
        # import pdb; pdb.set_trace()
        if not obj.locked:
            obj.expand_component_layout()
            message = "Función %s realizada" % obj.alias
            modeladmin.message_user(request, message, level=messages.SUCCESS)
        else:
            message = _("el id:%s, %s no se carga porque está bloqueado") % (obj.id, obj.name)
            modeladmin.message_user(request, message, level=messages.warning)
    return
ac_expand_component_layout.short_description = "Expandir Layout con sus Componentes"

