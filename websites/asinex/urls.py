
import os
from importlib import import_module
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView

# from .apigrql import schema
from .apis.apirest import router

# from .front.index1 import index1
from django.views.generic import TemplateView
# import pdb; pdb.set_trace()

num_admin_site = settings.NUM_ADMIN_SITE
# site_name = settings.SITE_NAME
prefix = settings.PREFIX_URL
html_index = settings.HTML_INDEX


if num_admin_site == "0" :
    #-----------------------
    # admin de django
    #------------------------
    # admin_site_activo = admin.site
    admin.autodiscover()
    # prefix = ""
    admin_site_activo = admin.site
else:

    AdminSiteActivo = getattr(import_module(
        'apps_admin.main%s.sites' % num_admin_site), 'AdminSite%s' % num_admin_site)
    admin_site_activo = AdminSiteActivo(name=settings.SITE_NAME)
    admin_site_activo.register_models()



urlpatterns = []

if True: # True: # settings.RUNSERVER:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    # path("%sindex1/" % prefix, index1, name="index1"),
    path('', TemplateView.as_view(template_name='%s.html' % html_index)),
    # path('index0/', TemplateView.as_view(template_name='index0.html')),
    path('index01/', TemplateView.as_view(template_name='index01.html')),
    path('index02/', TemplateView.as_view(template_name='index02.html')),

    #-----------------------------------
    # path('%sadmin/doc/' % prefix, include('django.contrib.admindocs.urls')),
    # path('%sadmin/' % prefix, admin.site.urls),
    #--------------------------
    # path('%s/doc/' % prefix, include('django.contrib.admindocs.urls')),
    # path('%sadmin/doc/' % prefix, include('django.contrib.admindocs.urls')),
    #-------------------------
    path('%sapirest/' % prefix, include(router.urls)),
    #---------------------------------------
    # path('%sapigrql/' % prefix, csrf_exempt(GraphQLView.as_view(
    #     graphiql=True,  schema=schema))),
    #----------------------
    path('%sckeditor/' % prefix, include('ckeditor_uploader.urls')),
    #-----------------------------
    path(prefix, admin_site_activo.urls),

]

