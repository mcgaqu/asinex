import os, sys, io # ??
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import get_wsite, print_msg
from ..models import Layout, Component


def gen_index_html(root, html_file):
    # import io # ???
    # file = open(html_file, 'a')
    
    import pdb; pdb.set_trace()
    with open(html_file, 'w') as file:
        html_file_part = os.path.join(
            settings.SITE_DIR, 'wapps', 'templates', "%s_0.html" % (root.root_alias))
        with io.open(html_file_part, 'r') as file_part: 
                # file_part = open(html_file_part, 'r')
                    text = file_part.read()
                    file.write(text)
    #-----------------------------------    
    with open(html_file, 'a') as file:
        for part in [1,2,3,4,5,6,7,8,9]:
            html_file_part = os.path.join(
                settings.SITE_DIR, 'wapps', 'templates', "%s_%s.html" % (root.root_alias, part))
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
    html_file = os.path.join(settings.SITE_DIR, 'wapps', 'templates', "%s.html" % root.root_alias)
    # gen_index_html(root, html_file)
    # return
    with open(html_file, 'r') as file:
        lines = file.readlines()
        # asumimos que no haya mas de un id= en cada linea
        # y que están en la misma línea el label y los attrs id, name y src/href en este orden
        conta_lin = 0
        
        # import pdb; pdb.set_trace()
        print_msg("=========================================================")
        for x in lines[:33]:
            
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
                grade = 'noId'
                last_alias = "lin%04d" % conta_lin
                sort = "%04d" % conta_lin
                #-----------------
                active = False
                # internal= True
            else:
                # num_int = conta_lin
                # import pdb; pdb.set_trace()
                active = True
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
                    sort = "%04d" % conta_lin
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
                    
                #----------------------------------
                if not 'name=' in line:
                    name = last_alias.upper()
                else:
                 # asumimos que siempre existe el ;
                    name = list_line[2].split('"')[1]
                #-----------------------------
                # params posibles
                #    - tags para setAttrs:
                #    - text1 o content para innerHTML
                #    - text2 para src/href
                #    - 
                #
                # 
                # 
                #         
                if 'mark=' in line:
                    xx = list_line[3].split('"')[1]
                    mark = xx.split(':')[0]
                    if len(xx.split(':'))>1:
                        params = xx.split(':')[1]
                if 'marki18n=' in line:
                    xx = list_line[4].split('"')[1]
                    marki18n = xx.split(':')[0]
                    if len(xx.split(':'))>1:
                        paramsi18n = xx.split(':')[1]
                #---------------------------

            try:
                page = Page.objects.get(num_int=conta_lin,
                    wsite=root.wsite, root_alias=root.root_alias, 
                    parent=parent, last_alias=last_alias)
            except Page.DoesNotExist:
                page = Page(num_int=conta_lin,
                    wsite=root.wsite, root_alias=root.root_alias, 
                    parent=parent, last_alias=last_alias)
            page.grade = grade
            page.num_int = conta_lin
            page.sort = sort
            page.active = active
            page.name = name
            page.mark = mark
            page.params = params
            page.marki18n = marki18n
            page.paramsi18n = paramsi18n
            #--------------------
            page.text5 = line
            # page.internal = True
            # page.active = False # ?????                    
            page.save() # generar i18n si toca = si marki18n

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







