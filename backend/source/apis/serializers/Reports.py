from apis.models import *
from apis.serializers import *
from rest_framework import serializers, exceptions
# from collections import namedtuple


class ResidentBillingSummarySerializer(serializers.ModelSerializer):
    trans = serializers.PrimaryKeyRelatedField(source='trans.TransDate', read_only=True)
    # FullName = serializers.SerializerMethodField()
    # trans = ChargesSerializers()
    # FullName = serializers.CharField(required=False)
    cost = serializers.DecimalField(max_digits=60, decimal_places=2)
    # p = serializers.DecimalField(max_digits=60, decimal_places=2)
    # unitprice = serializers.DecimalField(max_digits=60, decimal_places=2)

    class Meta:
        model = ChargesSupply
        fields = [
            # 'id',
            'testing',
            'trans',
            'trans_id',
            'unitprice',
            'quantity',
            'productid',
            'Description',
            'cost',
            'p',
        ]
        # read_only_fields = ['LineNum', 'trans_id', 'user']
