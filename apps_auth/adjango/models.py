
from django.conf import settings
from django.db import models
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# from django.contrib.sites.models import Site
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.main1.models.modelbase import ModelBase
from apps_admin.main1.models.modeltree import ModelTree1

# Create your models here.

#----------------------------
# MODELOS MANAGE=FALSE para usar en los adminmodels
#----------------------------------------

class UserGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_user_groups'
        managed = False
        verbose_name = _('Grupo/Usuario')
        verbose_name_plural = _('Grupos/Usuarios')

    @property
    def alias(self):
        return "%s_%s" % (self.group.name, self.user.username)


    def __str__(self):
        return "%s - %s" % (self.group.name, self.user.username)
    
    def MC_user_first_name(self):
        return "%s" % self.user.first_name
    MC_user_first_name.short_description = _("Nombre y Apellidos")                        
        

class GroupPermission(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_group_permissions'
        managed = False
        verbose_name = _('Grupo/Permiso')
        verbose_name_plural = _('Grupos/Permisos')

    @property
    def alias(self):
        return "%s_%s" % (self.group.name, self.permission.name)


class UserPermission(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    permission = models.ForeignKey(Permission, on_delete=models.PROTECT)

    class Meta:
        db_table = 'auth_user_user_permissions'
        managed = False
        verbose_name = _('Usuario/Permiso')
        verbose_name_plural = _('Usuarios/Permisos')

    @property
    def alias(self):
        return "%s_%s" % (self.user.username, self.permission.name)


class Migration(models.Model):
    app = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    applied = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'django_migrations'
        managed = False
        verbose_name = _('Migration')
        verbose_name_plural = _('Migrations')

#=================================================
# MODELOS PROPS: ABSTRACTOS
#=====================================

class UserProp(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta(ModelBase.Meta):
        abstract = True
        verbose_name = _('Preferencia de Usuario')
        verbose_name_plural = _('Preferencias de Usuario')
        unique_together = ['user', 'alias']

    def default_prop(self):
        return [
            'biz', 'company'
        ]

class GroupProp(ModelBase):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta(ModelBase.Meta):
        abstract=True
        verbose_name = _('Preferencia de Grupo')
        verbose_name_plural = _('Preferencias de Grupo')
        unique_together = ['group', 'alias']

    def default_prop(self):
        return [
            'biz', 'company'
        ]


# --------------------------
# Menus: Modelos Abstractos
#-----------------------------------

class Menu(ModelBase):
    # biz = models.ForeignKey(Biz, on_delete=models.CASCADE, 
    #                                 null=True, blank=True)

    # company = models.ForeignKey(Company, on_delete=models.CASCADE, 
    #                                 null=True, blank=True)

    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                                    null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                    null=True, blank=True)

    path = models.CharField(max_length=250, null=True, blank=True)

    class Meta(ModelBase.Meta):
        abstract=True
        verbose_name = _('Menu')
        verbose_name_plural = _('4. Menus')
        # unique_together= (('company', 'group', 'alias'),)

    def __str__(self):
        return "%s - %s" % (self.alias, self.name)


    def ME_num_items(self):
        return self.menuitem_set.count()
    ME_num_items.short_description = _("Nº Opciones")

    def MU_MenuItem(self):
        href = "/%s/companies/menuitem/?menu__id=%s" % (settings.SITE_NAME, self.id)
        return format_html('<a href="{}">({}) IR</a>', href, self.ME_num_items())
    MU_MenuItem.short_description = _("Opciones Menú") 

    def ME_num_active_items(self):
        return self.menuitem_set.filter(active=True).count()
    ME_num_active_items.short_description = _("Nº Opciones Activas")

    def MU_active_MenuItem(self):
        href = "/%s/companies/menuitem/?menu__id=%s&active=1" % (settings.SITE_NAME, self.id)
        return format_html('<a href="{}">({}) IR</a>', href, self.ME_num_active_items())
    MU_active_MenuItem.short_description = _("Opciones Activas") 

    def delete(self):
        self.menuitem_set.all().update(parent=None)
        super().delete()

    def get_menu_list(self):
        if not self.menuitem_set.count():
            return []
        apps = self.menuitem_set.filterl(level=1, active=True)
        return apps
        
class MenuItem(ModelTree1):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,     
                                    null=True, blank=True)
    path = models.CharField(max_length=250, null=True, blank=True)

    class Meta(ModelTree1.Meta):
        abstract=True
        verbose_name = _('Opción de Menú')
        verbose_name_plural = _('5. Opciones de Menú')
        unique_together= (('menu', 'parent', 'grade', 'sort', 'alias'),)
        ordering = ['menu__id', 'grade', 'sort']

    def __str__(self):
        return "%s - %s" % (
            self.menu, self.alias)

    def save(self, *args, **kwargs):
        if self.parent and self.parent.menu:
            self.menu=self.parent.menu
        super().save(*args, **kwargs)