from rest_framework import serializers, exceptions
from Relationships.models import Distributor


class DistributorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'
