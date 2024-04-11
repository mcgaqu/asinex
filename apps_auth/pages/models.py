
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

class DocAndImageMixin(object):
    #----------------------------------
    def MH_docfile_name(self):
        if self.docfile:
            return self.docfile.name
        return ""   
    MH_docfile_name.short_description = _("Nombre Doc")

    def MH_docfile_size(self):
        if self.docfile:
            return self.docfile.size
        return ""   
    MH_docfile_size.short_description = _("Tamaño Doc")

    def MH_docfile_url(self):
        if self.docfile:
            return self.docfile.url 
        return ""   
    MH_docfile_url.short_description = _("url del Doc")

    def MH_docfile_path(self):
        if self.docfile:
            return self.docfile.path
        return ""   
    MH_docfile_path.short_description = _("Ruta Doc")

    def MH_docfile_icon(self):
        return get_icon(self.docfile.url)
    
    def MH_docfile_open(self):
        # import pdb; pdb.set_trace()
        if self.docfile:
            etiq = "%s_%s" % (self.id, self.name)
            href = self.docfile.url
            # return format_html('<a href="{}">{}</a>', href, etiq)
            return format_html('<a target="_blank" href="{}">{}</a>', href, etiq)
        return "No hay documento"
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

    #-----------------------------------------------
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

    #------------------------------------------

    def MH_link_icon(self):
        return get_icon(self.link)
            
    def MH_link_open(self):
        if self.link:
            etiq = "%s_%s" % (self.id, self.nombre)
            href = self.link
            return format_html('<a href="%s">%s</a>' % (href, etiq))
        return ""


        
#--------------------------
# Component
#-----------------------------------

class DocAndImage(ModelTree1,DocAndImageMixin):
    wsite = models.ForeignKey(Wsite, on_delete=models.CASCADE, 
                                    null=True, blank=True)

    file_type = models.CharField(max_length=250,
                            choices = (
                              ('docfile', 'docfile'),
                              ('imagefile', 'imagefile'),                             
                            ) ,
                            null=True, blank=True)
   
    docfile = models.FileField('Fichero (pdf, xls, doc, svg..)', max_length=250, null=True, blank=True)
 
    imagefile = models.ImageField('Imagen', max_length=250,     
                                  width_field='imagewidth', height_field='imageheight',
                                  null=True, blank=True)
    imagefile_width = models.IntegerField(null=True, blank=True)
    imagefile_height = models.IntegerField(null=True, blank=True)

    linkfile = models.CharField(max_length=250, null=True, blank=True)  


    class Meta(ModelTree1.Meta):
        verbose_name= _("Documento / Imagen")
        verbose_name_plural= _("Documentos / Imágenes")
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

 
    def x_ME_num_pages(self):
        return self.page_set.count()
    x_ME_num_pages.short_description = _("Nº pages")



class PageMixin(object):

    def MH_field_richtext(self):
        if not self.field_richtext:
            return ""
        return format_html(self.field_richtext)

    def MH_content_edit(self):
        texto = ""
        # accion = 'MODIFICAR' if self.field_richtext else "AÑADIR"
        if self.content_type in ['text', 'richtext', 'html']: # self.mark and '__content' in self.mark:
            texto = '<span>Pulse Intro para %s: </span>' % 'EDITAR'
        return format_html(texto)
    MH_content_edit.short_description = _('Editar Página')


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


class Page(ModelTree1, PageMixin):

    wsite = models.ForeignKey(Wsite, on_delete=models.CASCADE, 
                              limit_choices_to="level=o",
          
                                    null=True, blank=True)
    html_label = models.CharField(max_length=20, null=True, blank=True)

    # ATRIBUTOS -----------------------
    # id = last_alias
    attrs = models.JSONField(null=True, blank=True)

    # attr_class = models.CharField(max_length=250, null=True, blank=True)
    # attr_style = models.CharField(max_length=250, null=True, blank=True)
    # attr_src = models.CharField(max_length=250, null=True, blank=True) 
    #    
    # # CONTENIDO DE CAMPO ------------------------
    content_type = models.CharField(max_length=20, 
                    choices=(
                        ('', ''),
                        ('char', 'char'), # i18n
                        ('text', 'text'), # i18n
                        ('richtext', 'richtext'), # i18n
                        ('html', 'html'),
                        ('children', 'children')
                    ),
                      null=True, blank=True)
    
    field_char = models.CharField('Texto Corto', max_length=250, null=True, blank=True)
    field_text = models.TextField('Texto largo', null=True, blank=True)
    field_richtext = RichTextField('HiperTexto', null=True, blank=True)
    field_html = models.TextField('Html1', null=True, blank=True)

    # CONTENIDO DE ACCIONES -------------------------

    content_action = models.CharField(max_length=150, null=True, blank=True)
    content_params = models.CharField(max_length=250, null=True, blank=True)
    # label_field: name_field

    # field_file = models.FileField('Imagen', max_length=250, null=True, blank=True)

    text1 = models.CharField('Texto1', max_length=250, null=True, blank=True)
    text2 = models.CharField('Texto2', max_length=250, null=True, blank=True)
    text3 = models.CharField('Texto3', max_length=250, null=True, blank=True)
    text4 = models.CharField('Texto4', max_length=250, null=True, blank=True)
    text5 = models.CharField('Texto5', max_length=250, null=True, blank=True)

    html1 = models.TextField('Html1', null=True, blank=True)
    html2 = models.TextField('Html2', null=True, blank=True)

    # traduccion ------------------------
    i18n_action = models.CharField(max_length=250, null=True, blank=True)
    i18n_params = models.CharField(max_length=250, null=True, blank=True)

    class Meta(ModelTree1.Meta):
        verbose_name = _('Página web')
        verbose_name_plural = _('Paginas web')
        unique_together= (('wsite', 'root_alias', 'alias'),)
        ordering = ('wsite','pos',)

    def __str__(self):
        return "%s" % (self.alias)
    

    def ME_num_i18n(self):
        return self.pagei18n_set.count()
    ME_num_i18n.short_description = _("Nº I18n")

    def MB_i18n(self):
        return (self.content_type in ['char', 'text', 'richtext'])
    MB_i18n.short_description = 'Traducir'
    MB_i18n.boolean = True

    def MC_pos_alias(self):
        clave = "" if not self.last_alias else self.last_alias
        return "%s____ %s" % (self.pos, clave)
    MC_pos_alias.short_description = "Pos - Clave"

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

    def save(self, *args, **kwargs):
        if not self.wsite:
            if self.parent:
                self.wsite = self.parent.wsite
            else:
                self.wsite = get_wsite(settings.SITE_NAME)
        self.internal = (
            self.attr_class or self.attr_style or self.attrs or self.content_actions)
        self.replace = self.MB_i18n
        
        # import pdb; pdb.set_trace()

        return super().save(*args, **kwargs)


    def get_languages(self):
        try:
            root = self.__class__.objects.get(
                wsite=self.wsite, root_alias=self.root_alias,
                level=0)
            if root.name:
                languages = root.name.split(',')
            else:
                languages = None
        except:
            languages = None
        return languages
    
    def create_i18n(self):
        if not self.MB_i18n:
            return
        languages = self.languages
        count = 0
        for lan in languages:
            count +=1
            try:
                # reg = LayoutI18n.objects.get(alias=aliasId)
                reg = PageI18n.objects.get(layout=self, sort=lan)
                if reg.locked:
                    continue
            except PageI18n.DoesNotExist:
                reg = PageI18n(layout=self, sort=lan)
            reg.grade = lan
            #----------------------------------
            reg.content_type = self.content_type
            reg.field_char = self.field_char
            reg.field_text = self.field_text
            reg.field_richtext = self.field_richtext

            reg.active = self.active
            # reg.content_action = self.content_action
            # reg.content_params = self.content_params
            #-----------------------
            reg.name = "[%s -->] %s" % (lan.upper(), self.name)
            # reg.tags = self.tags
            # reg.note = self.note
            #------------------------         
            #-----------------------------
            # reg.text1 = self.text1
            # reg.text2 = self.text2
            # reg.text3 = self.text3
            # reg.text4 = self.text4
            # reg.text5 = self.text5
            # reg.html1 = self.html1
            # reg.html2 = self.html2

            # reg.i18n_action = self.i18n_action
            # reg.i18n_params = self.i18n_params

            reg.save()
        return


class PageI18n(ModelBase, PageMixin):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, 
                                    null=True, blank=True)

    page_root_alias = models.CharField('página', max_length=50, null=True, blank=True)
    page_last_alias = models.CharField('clave', max_length=50, null=True, blank=True)
    pos = models.CharField(max_length=50, null=True, blank=True)
    
    # CONTENIDO CAMPO------------------------
    content_type = models.CharField(max_length=20, 
                    choices=(
                        # ('', ''),
                        ('char', 'char'),
                        ('text', 'text'),
                        ('richtext', 'richtext'),
                        # ('html', 'html'),
                        # ('children', 'children')
                    ),
                      null=True, blank=True)
    
    field_char = models.CharField('Texto Corto', max_length=250, null=True, blank=True)
    field_text = models.TextField('Texto largo', null=True, blank=True)
    field_richtext = RichTextField('HiperTexto', null=True, blank=True)
    field_html = models.TextField('Html1', null=True, blank=True)

    # # CONTENIDO MULTIPLE ------------------------
    # content_action = models.CharField(max_length=150, null=True, blank=True)
    # content_params = models.CharField(max_length=250, null=True, blank=True)
    # # label_field: name_field

    # text1 = models.CharField('Texto1', max_length=250, null=True, blank=True)
    # text2 = models.CharField('Texto2', max_length=250, null=True, blank=True)
    # text3 = models.CharField('Texto3', max_length=250, null=True, blank=True)
    # text4 = models.CharField('Texto4', max_length=250, null=True, blank=True)
    # text5 = models.CharField('Texto5', max_length=250, null=True, blank=True)

    # html1 = models.TextField('Html1', null=True, blank=True)
    # html2 = models.TextField('Html2', null=True, blank=True)
    # # traduccion ------------------------
    # i18n_action = models.CharField(max_length=250, null=True, blank=True)
    # i18n_params = models.CharField(max_length=250, null=True, blank=True)

    class Meta(ModelBase.Meta):
        verbose_name = _('Traducción')
        verbose_name_plural = _('Traducciones')
        unique_together= (('page', 'alias'),)
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

    def MC_page_name(self):
        if self.page:
            return self.page.name
        return ""
    MC_page_name.short_description = 'Texto Base'

    def MC_page_grade(self):
        if self.page:
            return self.page.grade
        return ""

    def MC_page_sort(self):
        if self.page:
            return self.page.sort
        return ""

    def MC_page_alias(self):
        if self.page:
            return self.page.alias
        return ""

    def MC_page_pos(self):
        if self.page:
            return self.page.pos
        return ""

    def save(self, *args, **kwargs):
        if self.page:
            self.alias = "%s__%s" % (self.page.alias, self.sort)
            self.pos = "%s__%s" % (self.page.pos, self.sort)
            self.page_root_alias = self.page.root_alias 
            self.page_last_alias = self.page.last_alias 
        super().save(*args, **kwargs)

