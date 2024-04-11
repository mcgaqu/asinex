from django.conf import settings
from django.contrib import admin
# from django.contrib.auth.models import Group
from apps_admin.main1.options import ModelAdmin1, ModelLin1
from apps_admin.utils.base import get_wsite
# from mod_base.configs.models import Config1, Config2
from .models import DocAndImage, Page, PageI18n
from .actions import get_app_actions

#------------------------------
# Component
#------------------------

class DocAndImageAdmin1(ModelAdmin1):
    model = DocAndImage
    
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
    actions = get_app_actions('DocAndImage')   

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
# Page
#------------------------

class PageI18nAdmin1(ModelAdmin1):
    model = PageI18n

    #------------------------------------
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        qs = super().get_queryset(request)
        qs = qs.filter(
            layout__wsite=get_wsite(), active=True,
            layout_root_alias=settings.HTML_INDEX)
        return qs



    list_display = ['pos',# 'sort',
        'alias',
        'page_last_alias', 'locked',
         # 'grade', 
         'MC_page_name', 'MC_language','name',
                        'MH_content_edit','locked']
    # list_display = list_display1 + ['mark', 'params']

    def x_get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display1
        else:
            return self.list_display1

    list_display_links = ['pos', 'alias', 'MH_content_edit',]

    list_editable = ['name', 'locked' ]


    list_filter = ['grade', 'locked', 'mark' ]
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ['page__wsite','page__root_alias', 'internal', 'active'] + self.list_filter
        else:
            return self.list_filter

    x_search_fields = [# 'grade', 
                     '^pos', '^alias', 
                     '^page__last_alias' ,'page__name', 'name', 'content' ]

    #---------------------------------------       
    search_fields = ['^pos', '^alias', '^page__last_alias', 'name', 
        # 'grade', 'mark', 'mark_i18n',
         ]
    search_help_text = "Busque por: pos, código, clave y nombre"
    ## 'alias', 'name', 'grade','sort', 'pos', 'mark'
    # fields = ['doctype','grade', 'sort', 'alias', 'name', 'mark', 'docfile', 'content',
    #      'active', 'locked', 'MH_content']
    actions = get_app_actions('PageI18n')
    


    def x_get_fieldsets1(self, request, obj=None):
        return 		('Identidad', {
			'fields': [	
                ('page', 'grade', 'sort'),
                ('page_root_alias','page_last_alias','alias'),
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
                        ('page','grade', 'sort'),
                        ('page_root_alias', 'page_last_alias','alias'),
                        ('active', 'internal', 'replace', 'locked'),
                        ('mark', 'params'),
                        ],
                    'classes': ['collapse']
                    }
                )

    def x_get_fieldsets_datos(self, request, obj):
        if obj and obj.params:
            # field_list = [('mark', 'params')] + obj.params.split(',')
            field_list = obj.params.split(',')
        else:
            
            field_list =[# ('mark', 'params'),
                'name', 'link', 'content', 'MH_content',
                'text1','text2','text3','text4','note1','note2']
            field_list = []
        return ('Datos', {'fields': field_list})

    def get_fieldsets_content(self, request, obj):
        field_list = ['content_type']
        if obj.content_type in ['char', 'text', 'richtext', 'html']:
            field_list.append('field_%s' % obj.content_type)
        return ('Datos', {'fields': field_list})

    def get_fieldsets(self, request, obj=None):
        return [self.get_fieldsets_identidad(request, obj),
                   self.get_fieldsets_content(request, obj)]

#---------------------------------------


    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['alias', 'sort', 'MH_content']
        else:
            return ['alias', 'sort', 'MH_content', 'mark', 'params']


    #-------------------------
    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        else:
            return super().has_add_permission(request)
            
    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return super().has_delete_permission(request, obj)


class PageI18nLin1(ModelLin1):
    model = PageI18n
    fields = ['alias', # 'mark', 'params', 
              'name', 'active'
              # 'content', 'MH_content', 'active', 'internal',
    # 'note', 'content' 
    ]
    
    readonly_fields = ['alias', # 'mark', 'params', 
                       'active']
    classes = [] # ['collapse']

class PageChildLin1(ModelLin1):
    model = Page
    fields = [# 'alias', 
        'grade', 'sort', 'active', 'internal', 'mark', 'name' ]
    classes = []

class PageAdmin1(ModelAdmin1):
    model = Page

    #------------------------------------
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        qs = super().get_queryset(request)
        qs = qs.filter(wsite=get_wsite(), 
            root_alias=settings.HTML_INDEX,
            replace=False,
            internal=True,
            locked=True,
            ## mark__in=['loadDocName', 'loadImageName']
           )
        return qs

    ordering = ('pos',)
    #------------------------------------------------       

    list_display1 = [# 'pos', 'last_alias',
                    'MC_pos_alias', 
                    'name', 'replace', 'active', 'internal', 
                    # 'MB_i18n', # 'replace', 
                    # 'locked',
                     ]
    list_display = list_display1 + [
                
                # 'sort', 'last_alias',
                # 'ME_num_children',
                # 'mark', 'params', # 'note', 
                # 'tags',
                # 'mark_i18n', 'params_i18n', 
                'wsite','root_alias', 'level', 
                'locked'
            ]

    def get_list_display(self, request):
        if request.user.is_superuser:
            return self.list_display
        else:
            return self.list_display1
    #---------------------------------------
    list_display_links = [# 'pos', 'last_alias', 
                          'MC_pos_alias',
                          ]

    #---------------------------------------
    x_list_editable1 = []
    list_editable = [
        # 'wsite','parent', 
        # 'sort', 'last_alias', 
        'active', 'internal',
        'name',
        # 'mark', 'params', 'tags',
        # 'mark_i18n', 'params_i18n', 
        # 'locked'
        ]
    x_list_editable = ['active', 'locked']
    
    def x_get_list_editable(self, request):
        if request.user.is_superuser:
            return self.list_editable
        else:
            return self.list_editable1
 
    #---------------------------------------
    list_filter1 = ['replace']
    list_filter = [ 'active', 'internal', 'replace', 'locked',
        # 'parent', 'grade',
        # 'mark', 'mark_i18n',
        
        'wsite', 'root_alias', 'level',]

    def get_list_filter(self, request):
        if request.user.is_superuser:
            return self.list_filter
        else:
            return self.list_filter1
            
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
                        # ('pos', 'alias'),
                        ('active', 'internal', 'replace', 'locked'),
                        # ('mark', 'params'),
                        # ('mark_i18n', 'params_i18n'),
                       
                        # 'docfile',
                        ],
                    'classes': ['collapse']
                    }
                )

    def x_get_fieldsets_datos(self, request, obj):
        if obj and obj.params:
            # field_list = [('mark', 'params')] + obj.params.split(',')
            field_list = obj.params.split(',')
        else:
            
            field_list =[# ('mark', 'params'),
                'name', 'link', 'content', 'MH_content',
                'text1','text2','text3','text4','note1','note2']
            field_list = []
        return ('Datos', {'fields': field_list})
 
    def get_fieldsets_content(self, request, obj):
        field_list = ['content_type']
        if obj.content_type in ['char', 'text', 'richtext', 'html']:
            field_list.append('field_%s' % obj.content_type)
        return ('Datos', {'fields': field_list})



    def get_fieldsets(self, request, obj=None):
        return [self.get_fieldsets_identidad(request, obj),
                   self.get_fieldsets_content(request, obj)]
            
    readonly_fields = [# 'pos', 'alias', 
                       'MH_field_richtext']

    inlines = [# LayoutChildLin1, 
               PageI18nLin1]

    def get_inlines(self, request, obj):
        if not request.user.is_superuser:
            return []
        elif not obj or not obj.replace:
            return []
        return self.inlines
    #-------------------------
    def has_add_permission(self, request):
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
    admin.site.register(DocAndImage) #, ComponentAdmin1)
    admin.site.register(Page) #,LayoutAdmin1)
    admin.site.register(PageI18n) #, LayoutI18nAdmin1)

