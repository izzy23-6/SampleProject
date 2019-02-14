from django_filters import rest_framework as filters
from django.db.models import F
from .serializers import *


class MyFilterBackend(filters.DjangoFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        user = request.user
        custparent = request.query_params.get('custparent', None)
        return queryset.filter(custparent__facility__pk=user.pk, custparent=custparent)

class MyFilterBackendCust(filters.DjangoFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        user = request.user
        custparent = request.query_params.get('custparent', None)
        if custparent:
            return queryset.filter(facility=user.pk, custparent=custparent).prefetch_related('facility')
        else:
            return queryset.filter(facility__pk=user.pk)

