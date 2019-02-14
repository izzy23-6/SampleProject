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
# from ..filters import *


class ChargesSupplyFilters(FilterSet):
    userLocation = filters.CharFilter(method="filter_by_userLocation")
    minDate = filters.CharFilter(method="filter_by_minDate")
    maxDate = filters.CharFilter(method="filter_by_maxDate")

    class Meta:
        model = ChargesSupply
        fields = ('userLocation',)

    def filter_by_userLocation(self, queryset, name, value):
        user = self.request.user
        queryset = queryset.filter(trans__custparent=value)
        return queryset

    def filter_by_minDate(self, queryset, name, value):
        queryset = queryset.filter(trans__TransDate__gte=value)
        if queryset.exists() is not True:

            return queryset.model.objects.none()
        return queryset

    def filter_by_maxDate(self, queryset, name, value):
        queryset = queryset.filter(trans__TransDate__lte=value)
        return queryset


class ChargesSupplyViewSet(viewsets.ModelViewSet):
    queryset = ChargesSupply.objects.select_related('trans', 'trans__patient').all()
    serializer_class = ChargesSupplySerializers
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ChargesSupplyFilters
    ordering = ('-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
