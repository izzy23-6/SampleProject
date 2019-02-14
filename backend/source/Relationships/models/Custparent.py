from django.db import models
from django.conf import settings

# User = settings.AUTH_USER_MODEL


class Custparent(models.Model):
    custparent                 = models.BigAutoField(primary_key=True)
    # employees                  = models.ManyToManyField(User)
    name                       = models.CharField(max_length=255)
    comm_queue                 = models.CharField(max_length=128, blank=True, null=True)
    email                      = models.CharField(db_column='EMail', max_length=255, blank=True,                                      null=True)
    invoice_email              = models.CharField(db_column='Invoice_EMail', max_length=128, blank=True,                              null=True)
    portal_id                  = models.IntegerField(blank=True, null=True)
    sentupdate                 = models.DateTimeField(db_column='SentUpdate', blank=True, null=True)
    webaddress                 = models.CharField(max_length=255, blank=True, null=True)
    webext                     = models.CharField(max_length=3, blank=True, null=True)
    passcode                   = models.CharField(db_column='PassCode', max_length=128, blank=True,                                   null=True)
    autoapprove                = models.IntegerField(db_column='AutoApprove', blank=True, null=True)
    testaccount                = models.IntegerField(db_column='TestAccount', blank=True, null=True)
    privateemail               = models.IntegerField(db_column='PrivateEmail', blank=True, null=True)
    forcemanponum              = models.IntegerField(db_column='ForceManPONum', blank=True, null=True)
    procuretopay               = models.IntegerField(db_column='ProcureToPay', blank=True, null=True)
    medassets_member           = models.IntegerField(db_column='MedAssets_Member', blank=True,                                        null=True)
    medassets_facnum           = models.IntegerField(db_column='MedAssets_FacNum', blank=True,                                        null=True)
    hideglorder                = models.IntegerField(db_column='HideGLOrder', blank=True, null=True)
    searchall                  = models.IntegerField(db_column='SearchAll', blank=True, null=True)
    accountlabel               = models.CharField(db_column='AccountLabel', max_length=50, blank=True,                                null=True)
    inhouselabel               = models.CharField(db_column='InHouseLabel', max_length=50, blank=True,                                null=True)
    privatelabellogo           = models.CharField(db_column='PrivateLabelLogo', max_length=120,                                       blank=True, null=True)
    hin                        = models.CharField(db_column='HIN', max_length=9, blank=True, null=True)
    gln                        = models.CharField(db_column='GLN', max_length=13, blank=True, null=True)
    shiptoattn                 = models.CharField(db_column='ShiptoAttn', max_length=64, blank=True,                                  null=True)
    shiptoaddress              = models.CharField(db_column='ShiptoAddress', max_length=64, blank=True,                               null=True)
    shiptocity                 = models.CharField(db_column='ShiptoCity', max_length=64, blank=True,                                  null=True)
    shiptostateprov            = models.CharField(db_column='ShiptoStateProv', max_length=24,                                         blank=True, null=True)
    shiptopostalcode           = models.CharField(db_column='ShiptoPostalCode', max_length=24,                                        blank=True, null=True)
    shiptophone                = models.CharField(db_column='ShiptoPhone', max_length=24, blank=True,                                 null=True)
    shiptofax                  = models.CharField(db_column='ShiptoFax', max_length=24, blank=True,                                   null=True)
    multivendor                = models.IntegerField(db_column='MultiVendor', blank=True, null=True)
    lockformulary              = models.IntegerField(db_column='LockFormulary', blank=True, null=True)
    active                     = models.IntegerField(db_column='Active', blank=True, null=True)
    autoadded                  = models.IntegerField(db_column='AutoAdded', blank=True, null=True)
    allowpatientedit           = models.IntegerField(db_column='AllowPatientEdit', blank=True,                                        null=True)

    # objects = models.Manager()

    class Meta:
        # app_
        db_table = 'Custparent'
        # ordering = ('custparent',)

    @property
    def searchData(self):
        return str(self.custparent) + '   ' + self.name

    def __str__(self):
        return f'{str(self.custparent)} {self.name}'


