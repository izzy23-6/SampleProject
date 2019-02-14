from rest_framework import viewsets, generics, mixins, status
from rest_framework.views import APIView
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
import jwt
import json


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class EmployeeRelationViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeRelationSerializer
    queryset = Relation.objects.all()
