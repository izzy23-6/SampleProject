from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(IdPatient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('PersonID', 'SSNumber', 'FirstName', 'MiddleInitial', 'LastName', 'Address1', 'Address2', 'City', 'StateProv', 'PostalCode', 'Country', 'Language', 'Email', 'Cellphone', 'Active', 'Sex', 'Race', 'DateOfBirth', 'Age', 'ShipCode', 'RelationReference')

@admin.register(IdPatientAttr)
class PatientAttrAdmin(admin.ModelAdmin):
    list_display = ('Person', 'MedicalRecordID', 'InternalPatientReference', 'AdmitDate', 'BillingMethod', 'Payor', 'InsuranceID', 'MedicareID', 'MedicaidID', 'LocationID', 'Room', 'Bed', 'PriceGroup', 'Level', 'InContinenceSize')