from ..models import *
# from Relationships.models import Custparent
# from portal.models import Custparent
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'custparent',
            'email',
        ]
        depth=1

class EmployeeRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = [
            'user',
            'custparent'
        ]
