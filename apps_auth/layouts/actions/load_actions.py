import os, sys
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import get_wsite, print_msg
from ..models import Layout, Component


def gen_page(root):
    Page = Layout
    # ----------
    html_file = os.path.join(settings.SITE_DIR, 'wapps', 'templates', "%s.html" % root.root_alias)
    file = open(html_file, 'r')
    lines = file.readlines()
    # asumimos que no haya mas de un id= en cada linea
    # y que están en la misma línea el label y los attrs id, name y src/href en este orden
    conta = 0
    # import pdb; pdb.set_trace()
    print_msg("=========================================================")
    for x in lines:
        line = x.strip()
        conta +=1
        # print_msg(conta)
        # print_msg(line)
        print_msg("%03d: %s" % (conta,line))
        print_msg("-----------------------------------------------------")
        
        if "id=" in line:
            list_line = line.split(' ')
            grade = list_line[0]
            for attr in list_line[1:]:
                if "id=" in attr:
                    last_alias = attr[3:]

                if "name=" in attr:
                    name = attr[5:]# [5:]
                else:
                    name = ""
                if "src=" in attr or "href=" in attr:
                    link = attr
                else:
                    link = ""
            try:
                page = Page.objects.get(
                    wsite=root.wsite, root_alias=root.root_alias, last_alias=last_alias)
            except Page.DoesNotExist:
                page = Page(
                    wsite=root.wsite, root_alias=root.root_alias, last_alias=last_alias)
            page.grade = grade
            page.name = name
            page.link = link
            page.sort = "%03d" % conta
            page.save()
    return
    #--------------------------------------

def ac_gen_page(modeladmin, request, queryset):
    for obj in queryset:
        if not obj.parent and not obj.locked:
            gen_page(obj)
            message = "Función gen_page para %s realizada" % obj.root_alias
            modeladmin.message_user(request, message, level=messages.SUCCESS)
        else:
            message = _("la página:%s, %s no se carga porque no es raiz o está bloqueado") % (obj.id, obj.name)
            modeladmin.message_user(request, message, level=messages.warning)
        return
ac_gen_page.short_description = "Generar Página"







