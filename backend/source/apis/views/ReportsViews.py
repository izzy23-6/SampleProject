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
from decimal import *


class ReportsFilters(FilterSet):
    userLocation = filters.CharFilter(method="filter_by_userLocation")
    minDate = filters.CharFilter(method="filter_by_minDate")
    maxDate = filters.CharFilter(method="filter_by_maxDate")
    search_name = filters.CharFilter(method="filter_by_Name")

    class Meta:
        model = ChargesSupply
        fields = ('userLocation',)

    def filter_by_Name(self, queryset, name, value):
        query = value
        if query.isdigit():
            rr = Q(trans__patient__RelationReference__iexact=query) | Q(trans__patient__RelationReference__istartswith=query)
            qs = rr
        elif len(query.split()) > 1:
            fn, ln = query.split()
            s = Q(trans__patient__FirstName__iexact=fn, trans__patient__LastName__iexact=ln)
            qs = s
        else:
            # fn, ln = query.split()
            e = Q(trans__patient__FirstName__istartswith=query) | Q(trans__patient__LastName__istartswith=query)
            qs = e

        # qs = rr
        queryset = queryset.filter(qs).distinct()
        return queryset


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

class ResidentBillingSummaryViewset(viewsets.ModelViewSet):
    queryset = ChargesSupply.objects.select_related('trans', 'trans__patient', 'contractprice').all()
    serializer_class = ResidentBillingSummarySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = ReportsFilters
    # search_fields = ('FullName',)
    # ordering = ('-id')

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        results = response.data['results']
        prices = [Decimal(x['p'].translate(str.maketrans({',':'', '$':''}))) for x in results]
        quantity = [x['quantity'] for x in results]
        response.data['Total'] = "${:,.2f}".format(sum(prices))
        return response
