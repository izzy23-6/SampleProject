from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from django.shortcuts import *
from rest_framework.decorators import *
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import FilterSet


class CustparentViewset(viewsets.ModelViewSet):
    serializer_class = CustparentSerializers
    queryset = Custparent.objects.prefetch_related('facility').all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('custparent_id','name',)
