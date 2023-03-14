# -*- coding: utf-8 -*-
from importlib import import_module
from django.conf import settings
from django.utils import timezone

from django.contrib import messages
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import get_website
from ..models import Dataload #, Website



def ac_load_inidata(modeladmin, request, queryset):
    """
        1. Ejecutar carga inicial de funciones de carga en el sitio.
        La acción se podria ejecutar desde cualquir modelo prncipal: site, biz, company...
    """
    for obj in queryset:
        # import pdb; pdb.set_trace()
        # load_inidata(obj)
        obj.load_inidata()
        #----------------------------
        modeladmin.message_user(request, 'Carga inicial realizada', level=messages.SUCCESS)
    return
ac_load_inidata.short_description = "Cargar funciones de carga inicial"


#===========================

def ac_dataload_run(modeladmin, request, queryset):
    """
        1. Ejecutar la función definida en cada registro 
    """

    for obj in queryset:
        # import pdb; pdb.set_trace()
        if not obj.locked:
            obj.run()
            message = "Función %s realizada" % obj.alias
        else:
            message = _("el id:%s, %s no se ejecuta porque está bloqueado") % (obj.id, obj.name)
        modeladmin.message_user(request, message, level=messages.SUCCESS)
    return
ac_dataload_run.short_description = "Cargar Datos"
