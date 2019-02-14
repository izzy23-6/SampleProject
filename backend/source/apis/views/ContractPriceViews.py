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


class ContractPriceFilters(FilterSet):
    userLocation = filters.CharFilter(method="filter_by_userLocation")

    class Meta:
        model = ContractPrice
        fields = ('userLocation',)

    def filter_by_userLocation(self, queryset, name, value):
        user = self.request.user
        queryset = queryset.filter(custparent_id=value)
        return queryset


class ContractPriceViewset(viewsets.ModelViewSet):
    serializer_class = ContractPriceSerializers
    queryset = ContractPrice.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ContractPriceFilters
    # search_fields = ('productid', 'productid',)


class ContractPriceSearchDetailViewset(viewsets.ModelViewSet):
    serializer_class = ContractPriceSerializers
    queryset = ContractPrice.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ContractPriceFilters
    search_fields = ('^productid', '=productid',)
