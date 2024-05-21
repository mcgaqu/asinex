import os, sys, io # ??
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import get_wsite, print_msg
from ..models import Layout, Component


def gen_index_html(root, html_file):
    # import pdb; pdb.set_trace()
    with open(html_file, 'w') as file:
        html_file_part = os.path.join(
            settings.SITE_DIR, 'wapps', 'templates', 
            root.root_alias, "%s_0.html" % (root.root_alias))
        with io.open(html_file_part, 'r') as file_part: 
            text = file_part.read()
            file.write(text)
    #-----------------------------------  
    list_part = [1,2,3,4,5,6,7,8,9] 
    if not list_part:
        return
    with open(html_file, 'a') as file:
        for part in list_part:
            html_file_part = os.path.join(
                settings.SITE_DIR, 'wapps', 'templates', 
                root.root_alias, "%s_%s.html" % (root.root_alias, part))
            try:
                with io.open(html_file_part, 'r') as file_part: 
                # file_part = open(html_file_part, 'r')
                    text = file_part.read()
                    file.write(text)                    
            except:
                continue
    return   


def gen_page(root):
    Page = Layout
    # ----------
    html_file = os.path.join(
        settings.SITE_DIR, 'wapps', 'templates', 
        root.root_alias, "%s.html" % root.root_alias)
    gen_index_html(root, html_file)
    languages = root.grade.split(',')
    #-----------------------------
    with open(html_file, 'r') as file:
        lines = file.readlines()
        # asumimos que no haya mas de un id= en cada linea
        # y que están en la misma línea el label y los attrs id, name y src/href en este orden
        conta_lin = 0
        
        # import pdb; pdb.set_trace()
        print_msg("=========================================================")
        for x in lines: # [:33]:
            
            line = x.strip()
            conta_lin +=1
            text5 = line
            parent = root
            name = ''
            mark = ''
            params = ''
            marki18n = ''
            paramsi18n = ''
            # print_msg(conta)
            # print_msg(line)
            print_msg("%03d: %s" % (conta_lin,line))
            print_msg("-----------------------------------------------------")
            if not 'id=' in line:
                parent = None
                grade = 'noId'
                last_alias = "lin%04d" % conta_lin
                sort = "%04d" % conta_lin
                #-----------------
                # active = False
                # internal= True
            else:
                # num_int = conta_lin
                # import pdb; pdb.set_trace()
                # active = True
                list_line = line.split(' ')
                # grade = label
                grade = list_line[0]
                # last_alias = id=
                last_alias = list_line[1].split('"')[1]              
                #----------------- 
                xx = last_alias.split('-')
                if len(xx)==1:
                    # level = 1
                    # parent = root
                    sort = "0"
                elif len(xx) == 2:
                    # level = 1 + len(xx[1])
                    if len(xx[1]) == 1:
                        parent_last_alias = xx[0]
                    else:
                        parent_last_alias = "%s-%s" % (xx[0], xx[1][:-1])
                    try:
                        parent = Page.objects.get(
                            wsite=root.wsite, root_alias=root.root_alias, 
                            last_alias=parent_last_alias)
                        sort = last_alias[-1]
                    except Page.DoesNotExist:
                        parent = None
                        import pdb; pdb.set_trace()                    
                #----------------------------
                # if conta_lin == 64:
                #     import pdb; pdb.set_trace()
                if not 'name=' in line:
                    name = last_alias.upper()
                else:
                 # asumimos que siempre existe el :
                    name = list_line[2].strip().split('"')[1]
                #-----------------------------
                if 'mark=' in line:
                    # mark = list_line[3].split('"')[1]
                    xx = list_line[3].split('"')[1]
                    mark = xx.split(':')[0]
                    if not mark:
                        mark = "innerHTML"
                    if len(xx.split(':'))>1:
                        params = xx.split(':')[1]
                if 'marki18n=' in line:
                    # marki18n = list_line[4].split('"')[1]
                    xx = list_line[4].split('"')[1]
                    marki18n = xx.split(':')[0]
                    if not marki18n:
                        marki18n = "innerHTML"
                    if len(xx.split(':'))>1:
                        paramsi18n = xx.split(':')[1]
            #---------------------------
            if grade == "noId":
                continue
            #---------------------------------
            try:
                page = Layout.objects.get(num_int=conta_lin,
                    wsite=root.wsite, root_alias=root.root_alias, 
                    parent=parent, last_alias=last_alias)
            except Layout.DoesNotExist:
                page = Layout(num_int=conta_lin,
                    wsite=root.wsite, root_alias=root.root_alias, 
                    parent=parent, last_alias=last_alias)
            page.grade = grade
            page.num_int = conta_lin
            page.sort = sort
            # page.active = active
            page.name = name
            page.mark = mark
            page.params = params
            page.mark_i18n = marki18n
            page.params_i18n = paramsi18n
            #--------------------
            page.text5 = line
            # page.internal = True
            # page.active = False # ?????                    
            page.save() # generar i18n si toca = si marki18n
            #-----------------------
            if page.replace and languages:
                page.create_i18n(languages)

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
            modeladmin.message_user(request, message, level=messages.WARNING)
        return
ac_gen_page.short_description = "Generar Página"



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
                languages = root_obj.grade.split(',')
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




