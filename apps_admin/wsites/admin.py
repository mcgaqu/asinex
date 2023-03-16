from django.conf import settings
from django.contrib import admin

# from django.contrib.auth.models import Group
from apps_admin.main1.options import ModelAdmin1, ModelLin1
# from mod_base.configs.models import Config1, Config2

from .models import Wsite, Dataload
from .actions import get_app_actions


class WsiteAdmin1(ModelAdmin1):
    model = Wsite

    list_display = ['sort', 'grade', 'alias', 'name', 
        'active', 'internal', 'replace', 'locked']
      
    list_display_links = ['alias','name',]
 
    list_editable = [ 'active', 'internal', 'replace','locked']

    ordering = ('sort',)
    
    list_filter = ['internal', 'active', 'replace','locked' ]
    # search_fields = ['alias', 'name', 'grade','sort', 'pos', 'mark']

    actions = get_app_actions('Wsite')

    fields = list_display   


#------------------------------
# dataload
#------------------------

class DataloadAdmin1(ModelAdmin1):
    model = Dataload
    
    list_display = ['sort', 'grade', 'alias', 'name',
         'active', 'internal', 'replace', 'locked']
      
    list_display_links = ['alias','name',]
 
    list_editable = [ 'active', 'internal', 'replace','locked']

    ordering = ('sort',)

    list_filter = ['internal', 'active', 'replace','locked' ]
    # search_fields = ['alias', 'name', 'grade','sort', 'pos', 'mark']

    actions = get_app_actions('Dataload')
    
    fields = list_display


if settings.NUM_ADMIN_SITE == "0":
    admin.site.register(Wsite) # , WebsiteAdmin1)
    admin.site.register(Dataload) #, DataloadAdmin1)


