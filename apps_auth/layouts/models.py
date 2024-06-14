
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
        accion = "Editar textos multi-idioma"
        change = (self.replace) #  or self.params=='content' or self.params_i18n=='content')
        if change: # self.mark and '__content' in self.mark:
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

    def MH_mark_user(self):
        if not self.mark:
            mark = ''
        if self.mark == 'src':
            mark = 'la url de IMAGEN/FICHERO'
        elif self.mark == 'href':
            mark = 'la url de LINK'
        elif self.mark == 'innerHTML':
            mark = 'el texto'
        else:
            mark = self.mark
        # return 'Rellene el campo %s con %s' % (self.params, mark)
    
        texto = ""
        # change = (not self.internal) #  or self.params=='content' or self.params_i18n=='content')
        if mark: # self.mark and '__content' in self.mark:
            texto = '<span>Rellene el campo %s con %s </span>' % (self.params, mark)
            return format_html(texto)
        else:
            return ''
    MH_mark_user.short_description='Edit Attrs'
    
    def MC_marki18n_user(self):
        if not self.mark_i18n:
            return ""
        if self.mark_i18n == 'src':
            mark = 'la url de IMAGEN/FICHERO'
        elif self.mark_i18n == 'href':
            mark = 'la url de LINK'
        elif self.mark_i18n == 'innerHTML':
            mark = 'TEXTO'
        else:
            mark = self.mark_i18n
        return 'Rellene el campo %s con %s' % (self.params_i18n, mark)


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

    # root_alias --> nombre del fichero index.html
    # last_alias --> id= de cada elem en index.html
    # name --> label de cada elem del html
    # grade --> name de cada elem index.html

    # mark --> action de layout
    params = models.CharField(max_length=250, null=True, blank=True)
    mark_i18n = models.CharField(max_length=250, null=True, blank=True)
    params_i18n = models.CharField(max_length=250, null=True, blank=True)

    # tags --< ATributos
    # link --> src/href para labels img/a
    link = models.CharField(max_length=250, null=True, blank=True)   

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
    comp = models.ForeignKey(Component,  on_delete=models.CASCADE,
                                null=True, blank=True)   
 
    class Meta(ModelTree1.Meta):
        verbose_name = _('Página web')
        verbose_name_plural = _('Paginas web')
        unique_together= (('wsite', 'root_alias', 'alias'),)
        ordering = ('num_int',) # ('wsite','pos',)

    def __str__(self):
        return "%s" % (self.MC_parents_name())


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

    def MC_parents_name(self):
        # return "%s__%s" % (self.grade, self.sort)
        name = "" if not self.name else self.name
        if not self.parent:
            return name
        else:
            return "%s__%s" % (self.parent.MC_parents_name(), name)
 

    def save(self, *args, **kwargs):
        if not self.wsite:
            if self.parent:
                self.wsite = self.parent.wsite
            else:
                self.wsite = get_wsite(settings.SITE_NAME)
        #------------------------?????z
        self.internal = not(self.mark) #  or self.mark[0] == 'x'
        self.replace = not (not self.mark_i18n)
        self.active = (not self.internal or self.replace)
        # import pdb; pdb.set_trace()
        return super().save(*args, **kwargs)


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
            reg.name = self.name
            # reg.active = self.active
            reg.mark = self.mark_i18n
            reg.params = self.params_i18n
            # reg.content = "Traducir a %s %s" % (lan.upper(), self.content)
            # reg.text1 = "Traducir a %s %s" % (lan.upper(), self.text1)
            # reg.tags = self.tags # Attrs 
            # reg.note = self.note # texto html ??                        
            #-----------------------
            if False: # todavía no lo estoy usando
                reg.text2 = self.text2
                reg.text3 = self.text3
                reg.text4 = self.text4
                reg.text5 = self.text5
                reg.note1 = self.note1
                reg.note2 = self.note2
            reg.save()
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
 
    text1 = models.CharField(max_length=250, null=True, blank=True)
    text2 = models.CharField(max_length=250, null=True, blank=True)
    text3 = models.CharField('email / web', max_length=250, null=True, blank=True)
    text4 = models.CharField('botón Contenido', max_length=250, null=True, blank=True)
    text5 = models.CharField(max_length=250, null=True, blank=True)
    note1 = models.TextField(null=True, blank=True)
    note2 = models.TextField(null=True, blank=True)

    docfile = models.FileField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)  


    class Meta(ModelBase.Meta):
        verbose_name = _('Traducción')
        verbose_name_plural = _('Traducciones')
        unique_together= (('layout', 'alias'),)
        ordering = ('pos',)

    def MC_language(self):
        lans = {
            'de': 'ALEMAN',
            'en': 'INGLES',
            'es': 'ESPAÑOL',
            'fr': 'FRANCES',
            'dk': 'DANES'
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

