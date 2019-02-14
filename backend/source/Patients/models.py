from django.db import models
from source.CDR import SpanningForeignKey

""" IdPatient table Controller """
class IdPatient(models.Model):
    PersonID = models.BigAutoField(primary_key=True)
    custparent = SpanningForeignKey('portal.Custparent', on_delete=models.CASCADE, db_constraint=False)
    SSNumber = models.CharField(null=True, blank=True, max_length=11)
    FirstName = models.CharField(null=True, blank=True, max_length=85)
    MiddleInitial = models.CharField(null=True, blank=True, max_length=1)
    LastName = models.CharField(null=True, blank=True, max_length=60)
    # FullName                        = models.CharField(null=True, blank=True, max_length=85)
    # MiddleInitial                   = models.CharField(null=True, blank=True, max_length=1)
    # LastName                        = models.CharField(null=True, blank=True, max_length=60)
    Address1 = models.CharField(null=True, blank=True, max_length=60)
    Address2 = models.CharField(null=True, blank=True, max_length=60)
    Address3 = models.CharField(null=True, blank=True, max_length=60)
    City = models.CharField(null=True, blank=True, max_length=60)
    StateProv = models.CharField(null=True, blank=True, max_length=4)
    PostalCode = models.CharField(null=True, blank=True, max_length=10)
    Country = models.CharField(null=True, blank=True, max_length=60)
    Language = models.CharField(null=True, blank=True, max_length=60)
    Email = models.CharField(null=True, blank=True, max_length=60)
    Homephone = models.CharField(null=True, blank=True, max_length=12)
    # Fax                             = models.CharField(blank=True, max_length=12)
    Cellphone = models.CharField(null=True, blank=True, max_length=12)
    RelationReference = models.CharField(null=True, blank=True, max_length=24)
    # Pager                           = models.CharField(null=True, blank=True, max_length=12)
    # PagerEmail                      = models.CharField(null=True, blank=True, max_length=60)
    # WirelessEmail                   = models.CharField(null=True, blank=True, max_length=60)
    # WebURL                          = models.CharField(null=True, blank=True, max_length=60)
    # Active = models.PositiveIntegerField(null=True, blank=True)
    Active = models.BooleanField(default=True)
    Sex = models.CharField(max_length=1, blank=True, null=True)
    Race = models.CharField(null=True, blank=True, max_length=16)
    DateOfBirth = models.DateField(null=True, blank=True)
    Age = models.PositiveIntegerField(null=True, blank=True)
    ShipCode = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'id_patient'

    @property
    def FullName(self):
        return f'{self.FirstName} {self.LastName}'

    @property
    def searchPatients(self):
        return f'{str(self.PersonID)} - {self.FullName} - {self.RelationReference}'

    def __str__(self):
        return f'{self.FirstName} {self.LastName}'


class IdPatientAttr(models.Model):
    Person = models.ForeignKey(IdPatient, on_delete=models.CASCADE)
    # custparent                      = models.ForeignKey(Custparent, on_delete=models.CASCADE)
    MedicalRecordID = models.CharField(max_length=60, blank=True, null=True)
    InternalPatientReference = models.CharField(max_length=60, blank=True, null=True)
    AdmitDate = models.DateField(blank=True, null=True)
    DischargeDate = models.DateField(blank=True, null=True)
    BillingMethod = models.CharField(max_length=60, blank=True, null=True)
    Payor = models.CharField(max_length=120, blank=True, null=True)
    InsuranceID = models.CharField(max_length=60, blank=True, null=True)
    MedicareID = models.CharField(max_length=60, blank=True, null=True)
    MedicaidID = models.CharField(max_length=60, blank=True, null=True)
    LocationID = models.BigIntegerField(blank=True, null=True)
    Room = models.CharField(max_length=60, blank=True, null=True)
    Bed = models.CharField(max_length=60, blank=True, null=True)
    PriceGroup = models.CharField(max_length=60, blank=True, null=True)
    Level = models.CharField(max_length=12, blank=True, null=True)
    InContinenceSize = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'id_patient_attr'
