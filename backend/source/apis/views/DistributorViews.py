from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication



class DistributorViewset(viewsets.ModelViewSet):
    serializer_class = DistributorSerializers
    queryset = Distributor.objects.all()
