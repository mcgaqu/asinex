# -*- coding: utf-8 -*-

from rest_framework import serializers, generics, viewsets #, filters
from ..models import Page, PageI18n

#--------------------------
# Page
#-------------------------


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['url', 'id', 
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
         

class PageViewSet(viewsets.ModelViewSet):

    queryset = Page.objects.all().order_by('pos')
    serializer_class = PageSerializer

    filterset_fields = [# 'url',
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

    search_fields = [
        'name', 'note', 'content',
        'link', # 'docfile'
    ] 

    # ordering_fields = ['pos', 'alias', 'mark', 'mark_i18n', 'name']
    # ordering = ['pos']
    # filter_backends = (filters.SearchFilter,)


class PageI18nSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageI18n
        fields = [# 'url', 
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
        
 

class PageI18nViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = PageI18n.objects.all().order_by('pos')
    serializer_class = PageI18nSerializer

    filterset_fields = [# 'url', 
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
    
    search_fields = ['name', 'note', 'content'] # , 'typedoc__name'
    # ordering_fields = ['grade', 'sort', 'alias', 'name']
    # ordering = ['pos'] # ['layout__pos', 'grade']

