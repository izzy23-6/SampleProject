from django.db import models
from django.db.models import F, Q
from django.shortcuts import *
from source.CDR import SpanningForeignKey
from Patients.models import *
from Products.models import *
from users.models import *

""" Charges Table Controller """
class Charges(models.Model):
    TransID = models.BigAutoField(primary_key=True)
    TransDate = models.DateField()
    patient = models.ForeignKey(IdPatient, on_delete=models.CASCADE)
    # NumericTransDate        = models.IntegerField(blank=True, null=True)
    LastEditDateTime = models.DateTimeField(auto_now=True)
    custparent = SpanningForeignKey('portal.Custparent', on_delete=models.CASCADE, related_name="facilities")
    FromRecurTransID = models.PositiveIntegerField(blank=True, null=True)
    Exported = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'id_hcm_charges'


    def __str__(self):
        return f'{str(self.TransID)}'