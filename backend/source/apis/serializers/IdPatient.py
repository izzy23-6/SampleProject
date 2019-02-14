from rest_framework import serializers
from ..models import *
# from Patients.models import IdPatient, IdPatientAttr


class IdPatientSerializers(serializers.ModelSerializer):
    FullName = serializers.SerializerMethodField()
    searchPatients = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = IdPatient
        fields = '__all__'
        depth=1

    def get_FullName(self, obj):
        firstname = obj.FirstName
        lastname = obj.LastName
        return firstname + ' ' + lastname

class IdPatientAttrSerializers(serializers.ModelSerializer):
    class Meta:
        model = IdPatientAttr
        fields = '__all__'
