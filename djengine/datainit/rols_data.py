# -*- coding: utf-8 -*-

def get_menu_MASTER():
    from ..settings import PREFIX_URL
    from django.conf import settings
    PREFIX_URL = ''
    return [
        [
            ['#', 'Contenido'],
            [
                ['%sdataloads/component/%s/' % (PREFIX_URL, settings.SITE_ID), 'Componentes'],
                ['%sdataloads/layout/' % PREFIX_URL, 'Layouts'],
                ['%sdataloads/layouti18n/?level=0' % PREFIX_URL, 'Traducciones']
            ],
        ],
        # [
        #     ['#', 'Facturas'],
        #     [
        #         ['%splans/plandoc/' % PREFIX_URL, 'Ftras Previstas'],
        #         ['%splans/plandoctax/' % PREFIX_URL, 'Ftras: Impuestos'],
        #         ['%splans/plandocproduct/' % PREFIX_URL, 'Ftras: Productos'],
        #         ['%spersons/person/' % PREFIX_URL, 'Personas'],
        #         ['%sproducts/product/' % PREFIX_URL, 'Productos'],
        #     ],
        # ],
 
    ]

def get_menu_MANAGER():
    return get_menu_MASTER()   


def get_menu_EMPLOYEE():
    return [

    ]

def get_menu_CUSTOMER():
    return [
 
    ]



def get_ROLS_DATA():
    # from ..settings import PREFIX_URL
    from django.conf import settings
    site_name = settings.SITE_NAME
    index_url_master = "dataloads/layout/%s/change/" % settings.SITE_ID
    index_url_manager = "dataloads/layouti18n/%s/change/" % settings.SITE_ID
    return  {
        '%s_MASTER' % site_name: [index_url_master, get_menu_MASTER(),  {
                    'content_type__app_label__in': [
                        'auth', 
                        'websites', 
                        'adjango', 
                        'layouts',
                    ]
                }, [] # ['fran']
            ],
        '%s_MANAGER' % site_name: [index_url_manager, get_menu_MANAGER(),  {
                    'content_type__app_label__in': [
                        # 'auth', 
                        # 'websites', 
                        # 'adjango', 
                        'layouts',
                    ],
                    # 'content_type__model__in': ['layout', 'layouti18n'],
                    # 'code_name__contains': 'change'
                    # 'code_name__contains': 'view',
                }, ['fran','andrea']
            ],
    }

