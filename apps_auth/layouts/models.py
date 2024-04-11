
from importlib import import_module
from django.db import models
from django.conf import settings
from django.utils.translation import  gettext_lazy as _
from django.utils.html import format_html
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from apps_admin.main1.models.modelbase import ModelBase
from apps_admin.main1.models.modeltree import ModelTree1
from apps_admin.utils.base import get_wsite
from apps_admin.wsites.models import Wsite

def get_icon(url):
    icon = ""
    if '.pdf' in url:
        icon = 'img/pdf.png'
    elif '.doc' in url:
        icon = 'img/decw.png'
    elif '.xls' in url:
        icon = 'img/excel.png'
    else:
        icon = 'img/empty.png'
    return format_html('<img src="{}{}"  width=20 height=20 />',
                                settings.STATIC_URL,icon )

class Extradocfile(object):
    #----------------------------------
    def MH_docfile_name(self):
        if self.docfile:
            return self.docfile.name
        return ""   
    MH_docfile_name.short_description = _("Nombre")

    def MH_docfile_size(self):
        if self.docfile:
            return self.docfile.size
        return ""   
    MH_docfile_size.short_description = _("Tamaño")

    def MH_docfile_url(self):
        if self.docfile:
            return self.docfile.url 
        return ""   
    MH_docfile_url.short_description = _("url del Fichero")



    def MH_docfile_path(self):
        if self.docfile:
            return self.docfile.path
        return ""   
    MH_docfile_path.short_description = _("Ruta")

    def MH_docfile_icon(self):
        return get_icon(self.docfile.url)
    
    def MH_docfile_open(self):
        # import pdb; pdb.set_trace()
        if self.docfile:
            etiq = "%s_%s" % (self.id, self.name)
            href = self.docfile.url
            # return format_html('<a href="{}">{}</a>', href, etiq)
            return format_html('<a target="_blank" href="{}">{}</a>', href, etiq)
        return "No hay fichero"
        #----------------------------------
        # prefix = settings.STATIC_URL
        # prefix = settings.MEDIA_URL
        # prefix = "%s/" % settings.SITE_NAME
        # href = "%smedia/%s" % (settings.ROOT_PATH, self.fichero.url)

        # nombre = 'yes' if self.emp.activo else 'no'
        # icono = get_html_icono('admin/img/icon-%s.svg' % nombre)
        # return format_html('<button onclick="crearVentana();">{}</button>',"Nombre persona en G5")
        # return format_html('<a href="%s">%s</a>' % (href, etiq))
        #-----------------------
        return format_html('<img src="%s" />%s' % (self.docfile.url, etiq))

    def x_MH_docfile_display(self):
        if self.docfile:
            ancho = self.ancho or "200"
            alto = self.alto or "200"
            return format_html('<img src="%s" width="%s" height="%s"/>' % (
                self.docfile.url, ancho, alto))
        return "No hay Fichero"
    x_MH_docfile_display.short_description = _("Image")

    def MH_docfile_display_s(self):
        if self.docfile:
            return format_html('<img src="%s" width="120" height="100"/>' % (self.docfile.url))
        return "No hay Fichero"
    MH_docfile_display_s.short_description = _("Image")

    def MH_docfile_display_m(self):
        if self.docfile:
            return format_html('<img src="%s" width="400" height="400"/>' % (self.docfile.url))
        return "No hay Fichero"
    MH_docfile_display_m.short_description = _("Image")

    def MH_docfile_display_l(self):
        if self.docfile:
            return format_html('<img src="%s" width="800" height="800"/>' % (self.docfile.url))
        return "No hay Fichero"
    MH_docfile_display_l.short_description = _("Image")


    def MH_imagefile_size(self):
        if self.imagefile:
            ksize = int(self.imagefile.size/1024)
            return "%s ( ancho=%s x alto=%s)" % (
                ksize,
                self.imagewidth,
                self.imageheight,
            ) 
        else:
            return "No hay imagen"
    MH_imagefile_size.short_description = _("kilobytes")

    def MH_imagefile_display_s(self):
        if self.imagefile:
            return format_html('<img src="%s" height="40"/>' % (self.imagefile.url))
        return "No hay Imagen"
    MH_imagefile_display_s.short_description = _("Icono")

    def MH_imagefile_display_m(self):
        if self.imagefile:
            return format_html('<img src="%s" height="400"/>' % (self.imagefile.url))
        return "No hay Imagen"
    MH_imagefile_display_m.short_description = _("Imagen Mediana")

    def MH_imagefile_display_l(self):
        if self.imagefile:
            return format_html('<img src="%s" height="800"/>' % (self.imagefile.url))
        return "No hay Imagen"
    MH_imagefile_display_l.short_description = _("Imagen Grande")

    def MH_imagefile_url(self):
        if self.imagefile:
            return self.imagefile.url 
        return ""   
    MH_imagefile_url.short_description = _("url de la Imagen")

class ExtraLayout(Extradocfile):

    def MH_content(self):
        if not self.content:
            return ""
        return format_html(self.content)

    def MH_content_edit(self):
        texto = ""
        accion = 'MODIFICAR' if self.content else "AÑADIR"
        if self.params and (self.params != 'name'): # self.mark and '__content' in self.mark:
            texto = '<span>Pulse Intro para %s: </span>' % accion
        return format_html(texto)
    MH_content_edit.short_description = _('Edit Content')


    #---------------------------------

    def MH_link_icon(self):
        return get_icon(self.link)
            
    def MH_link_open(self):
        if self.link:
            etiq = "%s_%s" % (self.id, self.nombre)
            href = self.link
            return format_html('<a href="%s">%s</a>' % (href, etiq))
        return ""

    def MH_parent_name(self):
        if self.parent:
            if self.parent.name:
                name = self.parent.name.upper()
            else:
                name = ""
            return "%s:  %s" % (self.parent.__str__(), name)
        else:
            return "" 
    MH_parent_name.short_description='Nivel Superior'
        
#--------------------------
# Component
#-----------------------------------

class Component(ModelTree1, ExtraLayout):
    wsite = models.ForeignKey(Wsite, on_delete=models.CASCADE, 
                                    null=True, blank=True)


    content = RichTextField('Contenido',null=True, blank=True)

    text1 = models.CharField(max_length=250, null=True, blank=True)
    text2 = models.CharField(max_length=250, null=True, blank=True)
    text3 = models.CharField(max_length=250, null=True, blank=True)
    text4 = models.CharField(max_length=250, null=True, blank=True)
    text5 = models.CharField(max_length=250, null=True, blank=True)
    note1 = models.TextField(null=True, blank=True)
    note2 = models.TextField(null=True, blank=True)

    docfile = models.FileField('Fichero (pdf, xls, doc, svg..)', max_length=250, null=True, blank=True)

    imagewidth = models.IntegerField(null=True, blank=True)
    imageheight = models.IntegerField(null=True, blank=True)
    imagefile = models.ImageField('Imagen', max_length=250, 
                                  width_field='imagewidth', height_field='imageheight',
                                  null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)  


    class Meta(ModelTree1.Meta):
        verbose_name= _("Fichero")
        verbose_name_plural= _("Ficheros / Imágenes")
        unique_together= (('wsite','alias',),)
        ordering = ['pos']

    def __str__(self):
        return self.alias

    def save(self, *args, **kwargs):
        # import pdb; pdb.set_trace()
        dev = super().save(*args, **kwargs)
        if not self.wsite:
            self.wsite = get_wsite()
        if not self.last_alias:
            self.last_alias = "ID%s" % self.id
        
        return super().save(*args, **kwargs)

 
    def ME_num_layout(self):
        return self.layout_set.count()
    ME_num_layout.short_description = _("Nº ly")



class Layout(ModelTree1, ExtraLayout):
    wsite = models.ForeignKey(Wsite, on_delete=models.CASCADE, 
                                    null=True, blank=True)
    # front = models.CharField(max_length=250, null=True, blank=True)

    mark_i18n = models.CharField(max_length=250, null=True, blank=True)
    params = models.CharField(max_length=250, null=True, blank=True)
    params_i18n = models.CharField(max_length=250, null=True, blank=True)

    content = RichTextField('contenido', null=True, blank=True)

    text1 = models.CharField(max_length=250, null=True, blank=True)
    text2 = models.CharField(max_length=250, null=True, blank=True)
    text3 = models.CharField('email / web', max_length=250, null=True, blank=True)
    text4 = models.CharField('botón Contenido', max_length=250, null=True, blank=True)
    text5 = models.CharField(max_length=250, null=True, blank=True)
    note1 = models.TextField(null=True, blank=True)
    note2 = models.TextField(null=True, blank=True)

    # imgfile = models.FileField(max_length=250, null=True, blank=True)
    docfile = models.FileField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)  
    comp = models.ForeignKey(Component,  on_delete=models.CASCADE,
                                null=True, blank=True)   
 
    class Meta(ModelTree1.Meta):
        verbose_name = _('Página web')
        verbose_name_plural = _('Paginas web')
        unique_together= (('wsite', 'root_alias', 'alias'),)
        ordering = ('wsite','pos',)

    def __str__(self):
        return "%s" % (self.alias)



    def ME_num_i18n(self):
        return self.layouti18n_set.count()
    ME_num_i18n.short_description = _("Nº I18n")

    def MB_i18n(self):
        return self.replace
    MB_i18n.short_description = 'Translate'
    MB_i18n.boolean = True

    def MC_pos_alias(self):
        clave = "" if not self.last_alias else self.last_alias
        return "%s____ %s" % (self.pos, clave)
    MC_pos_alias.short_description = "Pos - Clave"

    def save(self, *args, **kwargs):
        if not self.wsite:
            if self.parent:
                self.wsite = self.parent.wsite
            else:
                self.wsite = get_wsite(settings.SITE_NAME)
        self.internal = not (not self.mark)
        self.replace = not (not self.mark_i18n)
        # import pdb; pdb.set_trace()
        return super().save(*args, **kwargs)

    def expand_layout(self):
        # if self.locked or not self.replace:
        #     return

        get_DATA = getattr(
            import_module('%s.datainit.layouts_data' % settings.WSITE_NAME),
            'get_LAYOUT_%s' % self.root_alias)
        data = get_DATA()

        root_obj = self
        wsite = root_obj.wsite
        root_alias = root_obj.root_alias
 
        #-----------
        # import pdb; pdb.set_trace()
        for data_row in data:
            pos_parent = data_row[0][:-3]
            sort = data_row[0][-2:]
            # grade = data_row[1]
            last_alias = data_row[1]
            active = data_row[2]
            locked = data_row[3]
            mark = data_row[4]
            mark_i18n = data_row[5]

            name = data_row[6] if len(data_row)>6 else ""
            tags = data_row[7] if len(data_row)>7 else ""
            note = data_row[8] if len(data_row)>8 else ""

            content = data_row[9] if len(data_row)>9 else ""
            params = data_row[10] if len(data_row)>10 else ""
            params_i18n = data_row[11] if len(data_row)>11 else ""

            link = data_row[12] if len(data_row)>12 else ""
            docfile = data_row[13] if len(data_row)>13 else ""

            text1 = data_row[14] if len(data_row)>14 else ""
            text2 = data_row[15] if len(data_row)>15 else ""
            text3 = data_row[16] if len(data_row)>16 else ""
            text4 = data_row[17] if len(data_row)>17 else ""
            text5 = data_row[18] if len(data_row)>18 else ""
            note1 = data_row[19] if len(data_row)>19 else ""
            note2 = data_row[20] if len(data_row)>20 else ""

            #--------------------------------
            # obtener el padre
            #----------------------
            try:
                lp = Layout.objects.get(wsite=wsite, root_alias=root_alias, pos=pos_parent)
            except Layout.DoesNotExist:
                print(data_row)
                import pdb; pdb.set_trace()
            try:
                lx = Layout.objects.get(wsite=wsite, parent=lp, sort=sort, 
                            last_alias=last_alias)
                
            except Layout.DoesNotExist:
                lx = Layout(wsite=wsite, parent=lp, sort=sort, last_alias=last_alias)
                
            lx.active = active
            lx.locked = locked
            lx.mark = mark
            lx.mark_i18n = mark_i18n

            lx.name = name
            lx.tags = tags
            lx.note = note
            lx.contet = content

            if not params and len(mark.split('__'))>1:
                lx.params = mark.split('__')[1]
            else:
                lx.params = params

            if not params_i18n and len(mark_i18n.split('__'))>1:
                lx.params_i18n = mark_i18n.split('__')[1]
            else:
                lx.params_i18n = params_i18n

            lx.link = link
            lx.docfile = docfile
            lx.text1 = text1
            lx.text2 = text2
            lx.text3 = text3
            lx.text4 = text4
            lx.text5 = text5
            lx.note1 = note1
            lx.note2 = note2

            lx.save()
            #-----------------------
            #------------------------------
            # languages = root_obj.params.split(',')
            
            languages = self.__class__.objects.filter(
                wsite=self.wsite, root_alias=self.root_alias,
                level=0
                # last_alias='languages', 
                )

            if languages:
                languages = languages[0].name
            if languages:
                languages = languages.split(',')
            else:
                languages = None

            if mark_i18n and languages:
                lx.create_i18n(languages)

        return

    def create_i18n(self, languages):
        # if not self.replace:
        #     return
        count = 0
        for lan in languages:
            count +=1
            try:
                # reg = LayoutI18n.objects.get(alias=aliasId)
                reg = LayoutI18n.objects.get(layout=self, sort=lan)
                if reg.locked:
                    continue
            except LayoutI18n.DoesNotExist:
                reg = LayoutI18n(layout=self, sort=lan)
            reg.grade = lan
            #----------------------------------
            reg.active = self.active
            reg.mark = self.mark_i18n
            reg.params = self.params_i18n
            #-----------------------
            reg.name = "[%s -->] %s" % (lan.upper(), self.name)
            reg.tags = self.tags
            reg.note = self.note
            #------------------------
        
            content = self.content
            reg.content = "Traducir a %s %s" % (lan.upper(), content)
            reg.docfile = self.docfile
            reg.link = self.link
 
            #-----------------------------
            reg.text1 = self.text1
            reg.text2 = self.text2
            reg.text3 = self.text3
            reg.text4 = self.text4
            reg.text5 = self.text5
            reg.note1 = self.note1
            reg.note2 = self.note2
            reg.save()
        return

    def expand_component_layout(self):
        try:
            # comp = Component.objects.get(biz=self.biz, alias=self.grade)
            # self.comp = comp
            # s = self.comp.componentprop_set.all()
            comps = Component.objects.filter(site=self.site, alias__startswith=self.component.alias)
            if comps:
                for comp in comps:
                    try:
                        lay = Layout.objects.get(site=self.site, parent=self, alias=comp.alias)
                    except Layout.DoesNotExist:
                        lay = Layout(site=self.site, parent=self, alias=comp.alias)
                        lay.grade = comp.name
                        lay.save()

        except Component.DoesNotExist:
            pass
        return    


class LayoutI18n(ModelBase, ExtraLayout):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, 
                                    null=True, blank=True)
    layout_root_alias = models.CharField('página', max_length=50, null=True, blank=True)
    layout_last_alias = models.CharField('clave', max_length=50, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)

    params = models.CharField(max_length=250, null=True, blank=True)
    params_i18n = models.CharField(max_length=250, null=True, blank=True)

    content = RichTextField('contenido', null=True, blank=True)
    docfile = models.FileField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)  

    text1 = models.CharField(max_length=250, null=True, blank=True)
    text2 = models.CharField(max_length=250, null=True, blank=True)
    text3 = models.CharField('email / web', max_length=250, null=True, blank=True)
    text4 = models.CharField('botón Contenido', max_length=250, null=True, blank=True)
    text5 = models.CharField(max_length=250, null=True, blank=True)
    note1 = models.TextField(null=True, blank=True)
    note2 = models.TextField(null=True, blank=True)

    class Meta(ModelBase.Meta):
        verbose_name = _('Traducción')
        verbose_name_plural = _('Traducciones')
        unique_together= (('layout', 'alias'),)
        ordering = ('pos',)

    def MC_language(self):
        lans = {
            'de': 'GERMAN',
            'en': 'ENGLISH',
            'es': 'SPANISH',
            'fr': 'FRANCE',
            'dk': 'DANSK'
        }
        if self.sort in lans.keys():
            return lans[self.sort]
        else:
            return "%s" % self.sort
    MC_language.short_description = 'Idioma'
    MC_language.admin_order_field = 'sort'

    def MC_layout_name(self):
        if self.layout:
            return self.layout.name
        return ""
    MC_layout_name.short_description = 'Texto Base'

    def MC_layout_grade(self):
        if self.layout:
            return self.layout.grade
        return ""

    def MC_layout_sort(self):
        if self.layout:
            return self.layout.sort
        return ""

    def MC_layout_alias(self):
        if self.layout:
            return self.layout.alias
        return ""

    def MC_layout_pos(self):
        if self.layout:
            return self.layout.pos
        return ""

    def save(self, *args, **kwargs):
        if self.layout:
            self.alias = "%s__%s" % (self.layout.alias, self.sort)
            self.pos = "%s__%s" % (self.layout.pos, self.sort)
            self.layout_root_alias = self.layout.root_alias 
            self.layout_last_alias = self.layout.last_alias 
        super().save(*args, **kwargs)

