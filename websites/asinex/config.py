import os

#=======================================
# CONFIGURACION PARA SETTINGS
#========================================
INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #--------------------------------
    # 'django.contrib.sites.apps.SitesConfig',
    #=======================
    'ckeditor',
    # 'ckeditor_uploader',
    # #--------------------------
    'django_filters',
    # #---------------------
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # 'markdown',
    #----------------------
    # 'graphene_django',
    #------------------
    # 'xlrd', 'xlwt',
    # 'django_docutils',
    # Pillow
    #=========================
    'apps_admin.wsites.apps.WsitesConfig',
    # 'apps_auth.adjango.apps.AdjangoConfig',
    # 'apps_auth.dataloads.apps.DataloadsConfig',
    'apps_auth.layouts.apps.LayoutsConfig',
    #-------------------------
    # 'djengine.wapps.'
    # 'websites.asinex.mod'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #------------------
    'corsheaders.middleware.CorsMiddleware',
    #---------------------
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #---------------------------------------
    # 'django.contrib.admindocs.middleware.XViewMiddleware',
    #------------------------------------
]





MODELADMINS1 = [


    ['django.contrib.auth', [
            ['User', 'UserAdmin', 1],
            ['Group', 'GroupAdmin', 1],
        ],
    ],    
    #------------------------------------
    ['apps_admin.wsites.apps.WsitesConfig', [
            ['Wsite', 'WsiteAdmin1', 1],
            ['Dataload', 'DataloadAdmin1', 2],
        ],
    ],
    #-------------------------------------------
    # ['apps_auth.adjango.apps.AdjangoConfig', [
    #        # ['ContentType', 'ContentTypeAdmin1', 1],
    #        # ['Permission', 'PermissionAdmin1', 1],
    #         ['User', 'UserAdmin', 1],
    #         ['Group', 'GroupAdmin', 1],
    #         # ['LogEntry', 'LogEntryAdmin1', 1],
    #         # ['Session', 'SessionAdmin1', 1],
    #         # ['Site', 'SiteAdmin1', 1],
    #     ],
    # ],
    #-----------------------------------
    ['apps_auth.layouts.apps.LayoutsConfig', [
            ['Component', 'ComponentAdmin1', 2],
            ['Layout', 'LayoutAdmin1', 2],
            ['LayoutI18n', 'LayoutI18nAdmin1', 2],
        ],
    ],
    #---------------------------------------


]

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



def get_param_settings(param, default=None):
    PARAMS = {
        'INSTALLED_APPS': INSTALLED_APPS,
        'MIDDLEWARE': MIDDLEWARE,
        # 'TEMPLATES': TEMPLATES,
        'AUTH_PASSWORD_VALIDATORS': AUTH_PASSWORD_VALIDATORS,
        'MODELADMINS1': MODELADMINS1,   
        #------
        # 'REST_FRAMEWORK':'',
        # 'CORS_ALLOW_ALL_ORIGINS': '',
        # 'CORS_ALLOW_HEADERS':'',
        # 'GRAPHENE': ''
    }

    if not param in PARAMS.keys():
        # print('PARAMETRO DEFAULT = %s: %s' % (param,default))
        print('settings PARAMETRO DEFAULT = %s: %s' % (param,''))
        return default
    # print('PARAMETRO DE CONFIG = %s: %s' % (param,PARAMS[param]))
    print('settings PARAMETRO DE CONFIG = %s: %s' % (param,''))
    return PARAMS[param]
