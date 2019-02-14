from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import FilterSet
from ..filters import *


class PatientFilters(FilterSet):
    Search = filters.CharFilter(method='filter_by_Name')
    class Meta:
        model = IdPatient
        fields = ('Search',)

    def filter_by_Name(self, queryset, name, value):
        query = value
        if query.isdigit():
            rr = Q(RelationReference__iexact=query) | Q(RelationReference__istartswith=query)
            qs = rr
        elif len(query.split()) > 1:
            fn, ln = query.split()
            s = Q(FirstName__iexact=fn, LastName__iexact=ln)
            qs = s
        else:
            e = Q(FirstName__istartswith=query) | Q(LastName__istartswith=query)
            qs = e
        queryset = queryset.filter(qs).distinct()
        return queryset


class IdPatientViewset(viewsets.ModelViewSet):
    serializer_class = IdPatientSerializers
    queryset = IdPatient.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering = ('-PersonID')
    search_fields = ('PersonID', 'FirstName', 'LastName', 'FullName', 'RelationReference',)


class IdPatientSearchViewset(viewsets.ModelViewSet):
    serializer_class = IdPatientSerializers
    queryset = IdPatient.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = PatientFilters


class IdPatientAttrViewset(viewsets.ModelViewSet):
    serializer_class = IdPatientAttrSerializers
    queryset = IdPatientAttr.objects.all()
