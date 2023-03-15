import environ
import os
from corsheaders.defaults import default_headers
from pathlib import Path
from .config import get_param_settings

env = environ.FileAwareEnv(
# env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str),
    ALLOWED_HOSTS=(list, ['127.0.0.1', 'localhost']),
    LANGUAGE_CODE=(str,'en-us'),
    # DATA_ROOT=(str),
    #-------------------------
    SITE_DOMAIN=(str),
    PREFIX_URL=(str),
    NUM_ADMIN_SITE=(str, '1'),
    #------------------
    SITE_ID=(int,1),
    COMPANY_ID=(int,1),
    BIZ_ID=(int,1),
    INDEX_ID=(int,1),
    


)

# =============================
# 01 - Build paths inside the project like this: BASE_DIR / 'subdir'.
# =======================================
SITE_DIR = Path(__file__).resolve(strict=True).parent
SITE_NAME = os.path.basename(SITE_DIR)

if os.path.basename(SITE_DIR.parent) == "websites":
    BASE_DIR = SITE_DIR.parent.parent
    WSITE_NAME = 'websites.%s' % (SITE_NAME)
else:
    BASE_DIR = SITE_DIR.parent
    WSITE_NAME = SITE_NAME

# NUM_ADMIN_SITE = os.environ.get('NUM_ADMIN_SITE', "1")
#-------------------------------------
# BASE_NAME = os.path.basename(BASE_DIR) # b2bmachine
# USER_DIR = BASE_DIR.parent.parent.parent
# USER_NAME = os.path.basename(USER_DIR)

# =============================
# Leer el fichero .env adecuado ??? Falta parametrizar???
# =======================================
# environ.Env.read_env(os.path.join(SITE_DIR, '.envs', '.env'))
environ.Env.read_env(os.path.join(SITE_DIR, '.env'))

#=============================
# 02  SECRET_KEY = 'django-insecure-8^__-1nmf%$^0^f271-(oio0_)n^t+-x*9%=hfytqy&#1m2hj='
#=============================
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
LANGUAGE_CODE = env('LANGUAGE_CODE')

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

SITE_DOMAIN = env('SITE_DOMAIN')
PREFIX_URL = env('PREFIX_URL', default='')
HTML_INDEX = env('HTML_INDEX')
NUM_ADMIN_SITE = env('NUM_ADMIN_SITE')


SITE_ID=env('SITE_ID')
COMPANY_ID=env('COMPANY_ID')
BIZ_ID=env('BIZ_ID')
INDEX_ID=env('INDEX_ID')

#=======================================
# 03. DATABASES AND CACHE
#========================================
# DATA_ROOT0 = os.path.join(BASE_DIR.parent.parent.parent.parent, 'DATA_SITE', SITE_NAME)
DATA_ROOT0 = os.path.join(BASE_DIR.parent, 'DATA_SITE', SITE_NAME)
DATA_ROOT = env('DATA_ROOT', default=DATA_ROOT0)
print('----------DATA_ROOT0=%s' % DATA_ROOT0)
print('----------DATA_ROOT =%s' % DATA_ROOT)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_ROOT, '%s.sqlite3' % SITE_NAME), 
    },
}

x_DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'b2b_%s' % SITE_NAME,
            'USER': 'b2b_%s' % SITE_NAME,
            'PASSWORD': '%s_b2b' % SITE_NAME,
            'HOST': '',
            'PORT': ''
        }
    }
# DATABASES1 = {
#     'default': env.db_url(
#         # 'SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db' 
#         'SQLITE_URL', default='sqlite:////%s/%s.dsqlite3' % (DATA_ROOT, SITE_NAME)         
#     )
# }

# DATABASES2 = {
#     'default': env.db(), # lee por defecto  DATABASE_URL
# }



DATABASE_ROUTERS = []

# x_CACHES = {
#     'default': env.cache(),  # lee CACHE_URL
#     'redis': env.cache_url('REDIS_URL')
# }


#=======================================
# 04. STATIC AND MEDIA FILES 
#========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "mod_admin/main1/templates"),
            os.path.join(SITE_DIR, "wapps/templates")
        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "apps_admin/main1/static"),
    os.path.join(SITE_DIR, "wapps/static")
]

# STATIC_URL = '/%s/static/' % SITE_NAME.lower()
STATIC_URL = '/static/'
STATIC_ROOT = '%s/' % os.path.join(DATA_ROOT ,'%s_static' % SITE_NAME)

# MEDIA_URL = '/%s/media/' % SITE_NAME.lower()
MEDIA_URL = '/media/'
MEDIA_ROOT = '%s/' % os.path.join(DATA_ROOT ,'%s_media' % SITE_NAME)
#-------------------------
# CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"
#---------------------------

ROOT_URLCONF = '%s.urls' % WSITE_NAME
WSGI_APPLICATION = '%s.wsgi.application' % WSITE_NAME   

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#----------------------------
# 05 APIS
#---------------------------

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'apps_admin.main1.restapi.PageNumberPagination1',
    'PAGE_SIZE': 100,
    #-----------------
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework.filters.OrderingFilter',
        
    ],
    'ORDERING_PARAM' : 'ordering',
    'SEARCH_PARAM' : 'search',
}

CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:3000",
#     "http://localhost:3000",
#     "http://localhost:58930",
#     "http://127.0.0.1:58930",
#     'http://localhost:49381',
# ]
#------------------------------------------
CORS_ALLOW_HEADERS = list(default_headers) + [
    # "my-custom-header",
    "contenttype",
]

GRAPHENE = {
    # ojo!!! hay que crear SCHEMA_OUTPUT desde SCHEMA
    # mapage.py graphql_schema --schema [SITE_NAMEX].schema.schema --out [SITE_NAMEX].data_schema.json
    'SCHEMA': '%s.apis.apigrql.schema' % WSITE_NAME, # Where your Graphene schema lives
    'SCHEMA_OUTPUT': '%s.data_schema.json' % WSITE_NAME,
    'SCHEMA_INDENT': 4,
    # 'MIDDLEWARE': 'graphene_django.debug.DjangoDebugMiddleware',
}


#================================
# SETCONF
#==========================
INSTALLED_APPS = get_param_settings('INSTALLED_APPS')
#--------
MIDDLEWARE = get_param_settings('MIDDLEWARE')
# TEMPLATES = get_param_settings('TEMPLATES')
AUTH_PASSWORD_VALIDATORS = get_param_settings('AUTH_PASSWORD_VALIDATORS')
MODELADMINS1 = get_param_settings('MODELADMINS1')
#-------------------
REST_FRAMEWORK = get_param_settings('REST_FRAMEWORK', REST_FRAMEWORK) 
CORS_ALLOW_ALL_ORIGINS  = get_param_settings('CORS_ALLOW_ALL_ORIGINS ', CORS_ALLOW_ALL_ORIGINS) 
CORS_ALLOW_HEADERS  = get_param_settings('CORS_ALLOW_HEADERS ', CORS_ALLOW_HEADERS) 
GRAPHENE = get_param_settings('GRAPHENE', GRAPHENE) 

#--------------------
def print_settings_env():
    params = {
        'SITE_DIR': SITE_DIR,
        'SITE_NAME': SITE_NAME,
        'BASE_DIR': BASE_DIR,
        'WSITE_NAME': WSITE_NAME,
        'TEMPLATES:': 'TEMPLATES'
    }
    env_params = {
        'DEBUG': DEBUG,
        'SECRET_KEY': SECRET_KEY,
        'ALLOWED_HOSTS':ALLOWED_HOSTS,
        'LANGUAGE_CODE': LANGUAGE_CODE,
        'DATA_ROOT':DATA_ROOT,
    #     #-------------------------
        'SITE_DOMAIN': SITE_DOMAIN,
        'PREFIX_URL': PREFIX_URL,
        'HTML_INDEX': HTML_INDEX,
        'NUM_ADMIN_SITE': NUM_ADMIN_SITE,
    #     #------------------
    #     SITE_ID,
    #     COMPANY_ID,
    #     BIZ_ID,
    #     INDEX_ID,
    #     LAYOUT_ID,
    }
    print('#---------------------------------')
    for param in params:
        print('setting PARAMENTRO = %s: %s' % (param, params[param]))
    print('#---------------------------------')
    for param in env_params:
        print('setting PARAMENTRO venv = %s: %s' % (param, env_params[param]))
    return
    print('#---------------------------------')
print_settings_env()