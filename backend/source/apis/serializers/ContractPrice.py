from rest_framework import serializers, exceptions
from portal.models import ContractPrice


class ContractPriceSerializers(serializers.ModelSerializer):
    searchProducts = serializers.CharField()

    class Meta:
        model = ContractPrice
        fields = '__all__'
        