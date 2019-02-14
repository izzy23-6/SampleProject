from django.shortcuts import get_object_or_404
from django.db.models import Q, F
from rest_framework import viewsets, generics, mixins, status
from rest_framework.permissions import BasePermission, IsAuthenticated
from ..views import *
from ..models import *
from django.conf import settings
from ..serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import FilterSet
from ..filters import *

# from rest_framework import request




class ChargesViewSet(viewsets.ModelViewSet):
    queryset = Charges.objects.select_related('patient').all()
    serializer_class = ChargesSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering =('-TransID')
    # permission_classes = (IsAuthenticated)
