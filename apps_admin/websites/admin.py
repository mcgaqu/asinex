from django.conf import settings
from django.contrib import admin

# from django.contrib.auth.models import Group
from apps_admin.main1.options import ModelAdmin1, ModelLin1
# from mod_base.configs.models import Config1, Config2

from .models import Website, Dataload
from .actions import get_app_actions


class WebsiteAdmin1(ModelAdmin1):
    model = Website

    list_display = ['sort', 'grade', 'alias', 'name', 
        'active', 'internal', 'replace', 'locked']
      
    list_display_links = ['alias','name',]
 
    list_editable = [ 'active', 'internal', 'replace','locked']

    ordering = ('sort',)
    
    list_filter = ['internal', 'active', 'replace','locked' ]
    # search_fields = ['alias', 'name', 'grade','sort', 'pos', 'mark']

    actions = get_app_actions('Website')

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
    admin.site.register(Website) # , WebsiteAdmin1)
    admin.site.register(Dataload) #, DataloadAdmin1)


