from django.apps import apps
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from ..views import *
from ..models import *
from ..serializers import *
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from django_filters.rest_framework import DjangoFilterBackend


class BaseViewSet(viewsets.ModelViewSet):

    @property
    def model(self):
        return apps.get_model(app_label=str(self.kwargs['app_label']), model_name=str(self.kwargs['model_name']))

    def get_queryset(self):
        model = self.kwargs.get('model')
        user = self.request.user
        return model.objects.filter(custparent__employees=user.pk)

    def get_serializer_class(self):
        BaseSerializer.Meta.model = self.kwargs.get('model')
        return BaseSerializer

    
