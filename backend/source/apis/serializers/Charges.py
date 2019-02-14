from django.db import models
from ..models import *
from rest_framework import serializers


class ChargesSerializers(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(source="patient.FullName", read_only=True)

    class Meta:
        model = Charges
        fields = [
            'TransID',
            'patient',
            'patient_id',
            'TransDate',
            'LastEditDateTime',
            'custparent',
            'FromRecurTransID',
            'Exported',
            # 'cs'
        ]
        # read_only_fields = ['patient_id']
        # depth = 1
