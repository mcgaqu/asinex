# -*- coding: utf-8 -*-
from ast import literal_eval
from importlib import import_module
from django.conf import settings
from django.contrib import messages
from django.db.models.fields import GenericIPAddressField
from django.utils import timezone
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext, gettext_lazy as _
from apps_admin.utils.base import print_msg
# from ..models import Group, User, Permission, GroupProp, UserProp, Menu, MenuItem



def load_rols():
       #-------
    mod_rols = import_module('%s.datainit' % settings.WSITE_NAME)
    get_rols_data = getattr(mod_rols, 'get_ROLS_DATA')
    rols_data = get_rols_data()
    count = 0
    for key, rols in rols_data.items():
        count +=1
       #---------------
       # rol-users
       #-------------------
        try:
            user = User.objects.get(username=key.lower())
        except User.DoesNotExist:
            user = User.objects.create_user(
                is_staff=True,
                username=key.lower(),
                password='_%s' % key.lower()
                )
        #------------------------------
        # groups con permisos
        #----------------------------
        try:
            group = Group.objects.get(name=key)
            print_msg("Ya existe el group = %s" % key)
        except Group.DoesNotExist:
            group = Group.objects.create(name=key)
            print_msg("Se ha creado el group = %s" % key)        
        #----------------------------
        filtro_perm = rols[2]
        print_msg(filtro_perm)
        if filtro_perm:
            perms = list(Permission.objects.filter(**filtro_perm))
        else:
            perms = list(Permission.objects.all())
        group.permissions.set(perms)
        group.save()
        #----------------------------
        # asociar grupos a rol-users
        #---------------------------------------
        user.groups.add(group)
        user.save() 
        #--------------------------
        # añadir users personalizados
        #--------------------------------------
        for name in rols[3]:
            try:
                user = User.objects.get(username=name)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    is_staff=True,
                    username=name,
                    password='_%s' % name
                    )              
            user.groups.add(group)
            user.save() 
    return
