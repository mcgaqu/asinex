# -*- coding: utf-8 -*-

from rest_framework import serializers, generics, viewsets #, filters
from ..models import Component, Layout, LayoutI18n

#--------------------------
# Layout
#-------------------------
class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component

        fields = ['url', 'id', 'website', 'alias',
            # 'root_alias', 'last_alias', 'alias', 
            'pos', 'sort',
            'active', 'internal',
            'name', 'note', 'content', 'mark', # 'mark_i18n'
            
        ]
         

class ComponentViewSet(viewsets.ModelViewSet):

    queryset = Component.objects.all().order_by('pos')
    serializer_class = ComponentSerializer

    filterset_fields = [# 'url',
            'id', 'website', 'alias',
            # 'root_alias', 'last_alias', 'alias', 
            'pos', 'sort',
            'active', 'internal',
            # 'name', 'note', 'content', 
            'mark', # 'mark_i18n'
        ]

    search_fields = ['name', 'note', 'content'] # , 'typedoc__name'

    # ordering_fields = ['pos', 'alias', 'mark', 'mark_i18n', 'name']
    # ordering = ['pos']
    # filter_backends = (filters.SearchFilter,)


#--------------------------
# Layout
#-------------------------
class LayoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layout
        x_fields = ['url', 'id', 
            # 'website', 
            'level','parent', 
            'sort', 'pos',
            'root_alias', 'last_alias', 'alias',
            #--------------------- 
            'active', 'internal', 'replace', 'locked',
            'mark', 'mark_i18n',
            'name', 'tags',
            'note', 'content',
            'params', 'params_i18n',
            #-----------------------
            'link', 'docfile' ,
            'text1', 'text2', 'text3', 'text4', 'text5',
            'note1', 'note2',
        ]
        fields = [# 'url', 
            'id', 
            'root_alias', 'last_alias', 
            # 'MC_parents_name', # ???
            'internal','locked',
            'mark', 'params',
            # 'text1', 'content',
            'text1', 'text2', 'note',
            'tags'
        ]
         

class LayoutViewSet(viewsets.ModelViewSet):

    queryset = Layout.objects.all().order_by('last_alias') # ('pos')
    serializer_class = LayoutSerializer

    x_filterset_fields = [# 'url',
            'id', # 'website', 
            'root_alias', 'last_alias', 'alias', 
            'pos', 'sort', 'level',
            #-------------------------------
            'active', 'internal', 'replace', 'locked',
            #--------------------------
            'mark', 'mark_i18n',
            'params', 'params_i18n',
            #-----------------------
            'link', # 'docfile' ,
            'text1', 'text2', 'text3', 'text4', 'text5',
            'note1', 'note2',
    ]
    filterset_fields = ['root_alias', 'locked', 'internal']

    # search_fields = ['name', 'note', 'content','link'] 

    # ordering_fields = ['pos', 'alias', 'mark', 'mark_i18n', 'name']
    # ordering = ['pos']
    # filter_backends = (filters.SearchFilter,)


class LayoutI18nSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LayoutI18n
        x_fields = [# 'url', 
                'id', 'layout',
                'sort', 'pos',
                'layout_root_alias', 'layout_last_alias', 'alias', 
                #-----------------------
                'active', 'internal', 'replace', 'locked',
                'mark', # 'mark_i18n',
                'params',  # 'params_i18n',
                'name', 'note', 'content', 
                #-----------------------
                'link', 'docfile' ,
                'text1', 'text2', 'text3', 'text4', 'text5',
                'note1', 'note2',
                ]
        
        fields = [# 'url', 
            'id',  'sort', # 'layout',
            'layout_root_alias', 'layout_last_alias', # 'alias',
            # 'MC_parents_name', # ???
            'locked', 'active',
            'mark', 'params',
            'text1', 'content',
        ]
 

class LayoutI18nViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = LayoutI18n.objects.all().order_by('layout_last_alias')
    serializer_class = LayoutI18nSerializer

    x_filterset_fields = [# 'url', 
                'id', 'layout',
                'layout_root_alias', 'layout_last_alias','alias', 
                'pos', 'sort',
                'active', 'internal',
                # 'name' 'note', 'content', 'mark',
            'mark', 'params', 
            #-----------------------
            'link', # 'docfile' ,
            'text1', 'text2', 'text3', 'text4', 'text5',
            'note1', 'note2',                ]
    filterset_fields = ['layout_root_alias', 'layout_last_alias', 'locked', 'active', 'sort']
    
    # search_fields = ['name', 'note', 'content'] # , 'typedoc__name'
    # ordering_fields = ['layout_last_alias', 'grade', 'sort', 'alias', 'name']
    # ordering = ['layout_last_alias'] # ['layout__pos', 'grade']

