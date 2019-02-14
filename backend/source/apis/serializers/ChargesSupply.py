from rest_framework import serializers, exceptions
from ..models import *
from ..serializers import *


class ChargesSupplySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    trans = ChargesSerializers()
    FullName = serializers.CharField(required=False)


    class Meta:
        model = ChargesSupply
        fields = [
            'id',
            'FullName',
            'trans',
            'trans_id',
            'LineNum',
            'LocationID',
            'BillingMethod',
            'ProductNum',
            'productid',
            'Description',
            'Quantity',
            'UnitID',
            'user',
            'contractprice',
        ]

        read_only_fields = ['LineNum', 'trans_id', 'user']


    def create(self, validated_data):
        """ Function that saves the serialized data """
        trans_data = validated_data.pop('trans')
        # supplies_data = validated_data.pop('chargesupply')
        trans, created = Charges.objects.get_or_create(
            **trans_data,
            # defaults={**trans_data}
        )
        chargesupply = ChargesSupply.objects.create(trans=trans, **validated_data)

        return chargesupply

    def update(self, instance, validated_data):
        """ Function that updates the already saved serialized data """
        instance.Quantity = validated_data.get('Quantity', instance.Quantity)
        instance.save()
        return instance

    # def to_representation(self, obj):
    #     rep = super(ChargesSupplySerializers, self).to_representation(obj)
    #     c_serializers = ChargesSerializers(obj.trans, context=self.context)
    #     c_rep = c_serializers.to_representation(obj.trans)
    #     for key in c_rep:
    #         rep[key] = c_rep[key]

    #     return rep
