from django.conf import settings
from django.contrib import admin
# from django.contrib.auth.models import Group
from apps_admin.main1.options import ModelAdmin1, ModelLin1
from apps_admin.utils.base import get_wsite
# from mod_base.configs.models import Config1, Config2
from .models import Component, Layout, LayoutI18n
from .actions import get_app_actions

#------------------------------
# Component
#------------------------
class x_ComponentChildLin1(ModelLin1):
    model = Component
    fields = ['sort', 'last_alias', 'name', 'docfile', 'active',
              'MH_docfile_url', 'MH_docfile_display'] # 'name', 'grade', 'sort']
    readonly_fields = ['MH_docfile_url', 'MH_docfile_display']


class ComponentAdmin1(ModelAdmin1):
    model = Component
    
    #------------------------------------------------       
    list_display = ['wsite',
        'alias', 'grade', 'name',# 'last_alias',
        'docfile','MH_docfile_size',
        'MH_docfile_display_s', 'MH_docfile_url',

        'imagefile', 'MH_imagefile_size',
        'MH_imagefile_display_s', 'MH_imagefile_url',
        ]
    def x_get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display
        else:
            return self.list_display  
    #---------------------------------------
    list_display_links = ['alias']
    def x_get_list_display_links(self, request):
        if request.user.is_superuser:
            return self.list_dispaly_links
        else:
            return self.list_display_links       
    #--------------------------------------- 
    list_editable = []

    #---------------------------------------
    list_filter = ['wsite', 'root_alias',
        'grade','active', 'internal','locked', 'replace']

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return self.list_filter
        else:
            return ['grade']
            
    #---------------------------------------       
    search_fields = ['^alias', 'last_alias', '^name', 
        # 'grade', 'mark', 'mark_i18n',
         ]
    search_help_text = "Busque por: código o nombre"

    #--------------------------
    actions = get_app_actions('Component')   

    def get_actions(self, request):
        actions = super()
        if request.user.is_superuser:
            return  super().get_actions(request)
        else:
            return None
    
    #------------------------------------
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        qs = super().get_queryset(request)
        qs = qs.filter(wsite=get_wsite()
                        # ,root_alias=settings.HTML_INDEX,
                        # level__gt=0
                        )
        return qs

    #==========================

    def get_fieldsets1(self, request, obj=None):
        fields = ['grade', 'name', 
                # ('docfile','MH_docfile_size','MH_docfile_url','MH_idocfile_display_m',),
                'imagefile','MH_imagefile_size', 'MH_imagefile_url',
                'MH_imagefile_display_s',
                'docfile', 
                ]        
        if request.user.is_superuser:
            fields = ['wsite', 'root_alias', 'last_alias' ] + fields + ['MH_docfile_path',]
        return (None, {'fields': fields })
    
    def x_get_fieldsets2(self, request, obj):
        field_list = obj.params.split(',')
        return ('Data', {'fields': field_list})
 
    def get_fieldsets(self, request, obj=None):
        return [self.get_fieldsets1(request)]

            
    readonly_fields = [# 'MH_content', 
            'MH_docfile_size', 'MH_docfile_path',
            'MH_docfile_url', 'MH_docfile_display_m',
            'MH_imagefile_size', 'MH_imagefile_url',
            'MH_imagefile_display_s', 
            'MH_docfile_path',
            ]

#------------------------------
# Layout
#------------------------

class LayoutI18nAdmin1(ModelAdmin1):
    model = LayoutI18n

    #------------------------------------
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        qs = super().get_queryset(request)
        qs = qs.filter(
            layout__wsite=get_wsite(), active=True,
            layout_root_alias='index3') # =settings.HTML_INDEX)
        return qs

    list_display1 = ['pos',# 'sort',
        'alias',
        'layout_last_alias',
         # 'grade', 
         'MC_layout_name', 'MC_language','name',
                        'MH_content_edit','locked']
    list_display = list_display1 + ['mark', 'params']

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display
        else:
            return self.list_display1

    list_display_links = ['pos', 'alias', 'MH_content_edit',]

    list_editable = ['name', 'locked' ]


    list_filter = ['grade', 'locked', 'mark' ]
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ['layout__wsite','layout_root_alias', 'internal', 'active'] + self.list_filter
        else:
            return self.list_filter

    x_search_fields = [# 'grade', 
                     '^pos', '^alias', 
                     '^layout_last_alias' ,'layout__name', 'name', 'content' ]

    #---------------------------------------       
    search_fields = ['^pos', '^alias', '^layout_last_alias', 'name', 
        # 'grade', 'mark', 'mark_i18n',
         ]
    search_help_text = "Busque por: pos, código, clave y nombre"
    ## 'alias', 'name', 'grade','sort', 'pos', 'mark'
    # fields = ['doctype','grade', 'sort', 'alias', 'name', 'mark', 'docfile', 'content',
    #      'active', 'locked', 'MH_content']
    actions = get_app_actions('LayoutI18n')
    


    def x_get_fieldsets1(self, request, obj=None):
        return 		('Identidad', {
			'fields': [	
                ('layout', 'grade', 'sort'),
                ('layout_root_alias','layout_last_alias','alias'),
                ('active', 'internal', 'replace', 'locked'),
                ('mark', 'params'),

                
               ],
            'classes': ['collapse']         
		})
    def x_get_fieldsets2(self, request, obj):
        if obj and obj.params:
            field_list = obj.params.split(',') # [('mark', 'params')] + 
        else:
            return None
            field_list =[# ('mark', 'params'),
                'name', 'link', 'content', 'MH_content',
                'text1','text2','text3','text4','note1','note2']
        return ('Data', {'fields': field_list})


    def x_get_fieldsets(self, request, obj=None):
        return [self.get_fieldsets1(request, obj),
                   self.get_fieldsets2(request, obj)]

#--------------------------------------

    def get_fieldsets_identidad(self, request, obj=None):
        return ('Identidad', {
                    'fields': [	
                        ('layout','grade', 'sort'),
                        ('layout_root_alias', 'layout_last_alias','alias'),
                        ('active', 'internal', 'replace', 'locked'),
                        ('mark', 'params'),
                        ],
                    'classes': ['collapse']
                    }
                )

    def get_fieldsets_datos(self, request, obj):
        if obj and obj.params:
            # field_list = [('mark', 'params')] + obj.params.split(',')
            field_list = obj.params.split(',')
        else:
            
            field_list =[# ('mark', 'params'),
                'name', 'link', 'content', 'MH_content',
                'text1','text2','text3','text4','note1','note2']
            field_list = []
        return ('Datos', {'fields': field_list})
 
    def get_fieldsets(self, request, obj=None):
        return [self.get_fieldsets_identidad(request, obj),
                   self.get_fieldsets_datos(request, obj)]

#---------------------------------------





    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['alias', 'sort', 'MH_content']
        else:
            return ['alias', 'sort', 'MH_content', 'mark', 'params']


    #-------------------------
    def has_add_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return super().has_add_permission(request)
            
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return super().has_delete_permission(request, obj)


class LayoutI18nLin1(ModelLin1):
    model = LayoutI18n
    x_fields = ['alias', 'mark', 'params', 'MC_mark_user', 
              # 'text1', 'content', 'active'
              # 'content', 'MH_content', 'active', 'internal',
    # 'note', 'content' 
    ]
    
    readonly_fields = ['alias', 'mark', 'params', 'MC_mark_user', 'active']
    classes = [] # ['collapse']

    def get_fieldsets(self, request, obj):
        if obj and obj.params:
            # field_list = [('mark', 'params')] + obj.params.split(',')
            field_list = ['alias', 'MC_mark_user'] + obj.params.split(',') + ['locked']
        else:
            
            field_list =[# ('mark', 'params'),
                'name', 'link', 'content', 'MH_content',
                'text1','text2','text3','text4','note1','note2']
            field_list = []
            
        return [(None, {'fields': field_list})]


class LayoutChildLin1(ModelLin1):
    model = Layout
    fields = [# 'alias', 
        # 'grade', 'sort', 
        'MC_parents_name',
        'name', 'mark',  'MC_mark_user',
        'text1', 
        'active', 'internal','locked']

    readonly_fields = ['MC_parents_name', # 'alias', 
        'grade', 'sort', 'active', 'internal', 'mark', 'name',
          'MC_mark_user', ]

    classes = []



class LayoutAdmin1(ModelAdmin1):
    model = Layout
    #------------------------------------
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            qs = super().get_queryset(request)
            qs = qs.filter(wsite=get_wsite(), 
                           level__gt=0,
                root_alias='index3', # settings.HTML_INDEX,
                active=True # = (not internal or replace)
                # internal = not mark
                # replace = not (not marki18n)                
            )
            return qs
    ordering = ('num_int',) # ('pos',)
    #------------------------------------------------       
    list_display = ['wsite', 'root_alias', 'grade', 'sort', 'pos', 'alias',
                    'num_int', 'last_alias', 'MC_parents_name', 'name',
                    'mark', 'params', 
                    'MC_mark_user', 
                    'text1', 
                    'mark_i18n', 'params_i18n',
                    # 'MC_marki18n_user',  
                    
                     'MH_content_edit', # 'content',
                    'internal', 'replace', 'active', 'locked']
    def get_list_display(self, request):
        if request.user.is_superuser:
            # return self.list_display
            return self.list_display
        else:
            return [# 'wsite', 'root_alias', 'grade', 'sort', 'pos', 'alias',
                    'num_int', 'last_alias', 'MC_parents_name',
                    'mark', # 'params', 
                    'MC_mark_user',
                    'text1',
                    # 'mark_i18n', 'params_i18n',
                    # 'MC_marki18n_user',   
                    # 'text2', # 'content',
                    'MH_content_edit',
                    'internal', 'replace', 'active', 'locked']
    #---------------------------------------
    list_display_links = ['num_int', 'last_alias', 'MC_parents_name',
                          'MH_content_edit']
    list_editable = ['locked', 'text1', ] #'content'
    #---------------------------------------
    list_filter = [ 'grade', 'active', 'internal', 'replace', 'locked',
        # 'parent', 'grade',
        'mark', 'mark_i18n', 'name',
        'wsite', 'root_alias', 'level',]

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return self.list_filter
        else:
            return ['active', 'internal', 'replace', 'locked',
                    'mark', 'mark_i18n', 'name']
    #---------------------------------------       
    search_fields = ['^pos', '^alias', '^last_alias', 'name', 
        # 'grade', 'mark', 'mark_i18n',
         ]
    search_help_text = "Busque por: pos, código, clave y nombre"
    #--------------------------
    actions = get_app_actions('Layout')   
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'lock_selected' in actions:
                del actions['lock_selected']
            actions = None
        return actions 
    
    #==========================
    def get_fieldsets_identidad(self, request, obj=None):
        return ('Identidad', {
                    'fields': [	
                        ('wsite','level', 'grade'),
                        ('parent', 'root_alias'),
                        ('sort', 'last_alias'),
                        ('pos', 'alias'),
                        ('active', 'internal', 'replace', 'locked'),
                        ('mark', 'params'),
                        ('mark_i18n', 'params_i18n'),
                       
                        # 'docfile',
                        ],
                    'classes': ['collapse']
                    }
                )


    def get_fieldsets_datos(self, request, obj):
        if obj and obj.params:
            # field_list = [('mark', 'params')] + obj.params.split(',')
            field_list = ['MC_mark_user'] + obj.params.split(',')
        else:
            
            field_list =[# ('mark', 'params'),
                'name', 'link', 'content', 'MH_content',
                'text1','text2','text3','text4','note1','note2']
            field_list = []
            
        return ('Datos', {'fields': field_list})
 
    def get_fieldsets(self, request, obj=None):
        return [self.get_fieldsets_identidad(request, obj),
                   self.get_fieldsets_datos(request, obj)]
            
    readonly_fields = ['MC_mark_user', # 'pos', 'alias', 
                       'MH_content']

    inlines = [# LayoutChildLin1,
                LayoutI18nLin1]

    def get_inlines(self, request, obj):
        if not obj:
            return []
        inlines = []
        # if obj.children.count():
        #     inlines.append(LayoutChildLin1)
        if obj.replace:
            inlines.append(LayoutI18nLin1)
        return inlines
        # if not request.user.is_superuser:
        #     return []
        # elif not obj or not obj.replace:
        #     return []
        # return self.inlines
    #-------------------------
    def has_add_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return super().has_delete_permission(request, obj)

if settings.NUM_ADMIN_SITE == "0":
    admin.site.register(Component) #, ComponentAdmin1)
    admin.site.register(Layout) #,LayoutAdmin1)
    admin.site.register(LayoutI18n) #, LayoutI18nAdmin1)


