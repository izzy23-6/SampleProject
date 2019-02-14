from portal.models import Custparent
from .User import UserSerializer
from rest_framework import serializers, exceptions


class CustparentSerializers(serializers.ModelSerializer):
    searchData = serializers.CharField()
    facility = UserSerializer(many=True)
    class Meta:
        model = Custparent
        fields = "__all__"
        # lookup_field='name'
