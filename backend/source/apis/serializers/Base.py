from ..models import *
from rest_framework import serializers, exceptions


class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'