# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework import serializers, generics, viewsets, filters
from ..models import User, Group, Site

from apps_admin.utils.base import get_apirest_fields

#----------------------------
# Idea para personaliza apis : --> Pendiente de prueba y mejora.
#--------------------------


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'id', 'username', 'email']
        # fields = get_api_fields(model, ['url', 'id', 'username', 'email'])
        fields = get_apirest_fields(User)

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    search_fields = ['alias', 'name']
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']
        fields = get_apirest_fields(Group)
        # fields = '__all__'



class GroupViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'url', 'name', 'domain']
        # fields = get_apirest_fields(Group)
        # fields = '__all__'



class SiteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer

    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)