import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import get_wsite
from ..models import Page





def gen_page(root):

    # ----------
    html_file_name = root.alias
    html_file = open(html_file_name, 'r')
    lines = html_file.readlines()
    # asumimos que no haya mas de un id= en cada linea
    for line in lines:
        list_line = line.split(' ')
        conta = 0        
        for word in list_line:
            if '<' in word:
                ini = True
                html_label = word[1:]
            elif 'id=' in word:
                conta +=1
                attrs = []
                last_alias = word[3:]
                try:
                    page = Page.objects.get(
                        wsite=root.wsite, root_alias=root.alias, last_alias=last_alias)
                except Page.DoesNotExist:
                    page = Page(
                        wsite=root.wsite, root_alias=root.alias, last_alias=last_alias)
                    page.html_label = html_label
                    page.save()
            elif 'class=' in word:
                attr_class = word[6:]
            elif 'style' in word:
                attr_style = word[6:]
            elif 'scr=' in word:
                attrs.append(['src',word[5:]])
            if '/>' in word or '</' in word:
                page.save()
        return
        #--------------------------------------


def ac_gen_page(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.parent and not obj.locked:
            obj.gen_page()
            message = "Función gen_page para %s realizada" % obj.root_alias
            modeladmin.message_user(request, message, level=messages.SUCCESS)
        else:
            message = _("la página:%s, %s no se carga porque no es raiz o está bloqueado") % (obj.id, obj.name)
            modeladmin.message_user(request, message, level=messages.warning)
        return
ac_gen_page.short_description = "Generar Página"





