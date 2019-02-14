from django.conf import settings
from django.db import models


class Distributor(models.Model):
    distributor = models.BigAutoField(primary_key=True)
    portal_id = models.BigIntegerField()
    gln = models.CharField(db_column='GLN', max_length=13, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=255, blank=True, null=True)
    comm_queue = models.CharField(max_length=128, blank=True, null=True)
    autoacknowledge = models.IntegerField(db_column='AutoAcknowledge')
    webaddress = models.CharField(max_length=255, blank=True, null=True)
    webext = models.CharField(max_length=3, blank=True, null=True)
    passcode = models.CharField(db_column='PassCode', max_length=128, blank=True, null=True)
    pmtattnto = models.CharField(db_column='PmtAttnTo', max_length=64, blank=True, null=True)
    pmtaddress = models.CharField(db_column='PmtAddress', max_length=64, blank=True, null=True)
    pmtcity = models.CharField(db_column='PmtCity', max_length=64, blank=True, null=True)
    pmtstateprov = models.CharField(db_column='PmtStateProv', max_length=24, blank=True, null=True)
    pmtpostalcode = models.CharField(db_column='PmtPostalCode', max_length=24, blank=True, null=True)
    pmtphone = models.CharField(db_column='PmtPhone', max_length=24, blank=True, null=True)
    pmtfax = models.CharField(db_column='PmtFax', max_length=24, blank=True, null=True)
    pmtlogo = models.CharField(db_column='PmtLogo', max_length=64, blank=True, null=True)
    pmttermsconditions = models.TextField(db_column='PmtTermsConditions', blank=True, null=True)
    pmtinvoiceinfo = models.TextField(db_column='PmtInvoiceInfo', blank=True, null=True)
    pmtinvoicelegal = models.TextField(db_column='PmtInvoiceLegal', blank=True, null=True)
    privatelabel = models.IntegerField(db_column='PrivateLabel', blank=True, null=True)
    privatelabellogo = models.CharField(db_column='PrivateLabelLogo', max_length=64, blank=True, null=True)
    privatelabelsalesurl = models.CharField(db_column='PrivateLabelSalesURL', max_length=255, blank=True, null=True)
    privatelabelsupporturl = models.CharField(db_column='PrivateLabelSupportURL', max_length=255, blank=True, null=True)
    privatelabelemailfrom = models.CharField(db_column='PrivateLabelEmailFrom', max_length=60, blank=True, null=True)
    privatelabelemailheader = models.TextField(db_column='PrivateLabelEmailHeader', blank=True, null=True)
    privatelabelemailfooter = models.TextField(db_column='PrivateLabelEmailFooter', blank=True, null=True)
    punchoutenabled = models.IntegerField(db_column='PunchoutEnabled', blank=True, null=True)
    punchouturl = models.CharField(db_column='PunchoutURL', max_length=125, blank=True, null=True)
    punchoutsecret = models.CharField(db_column='PunchoutSecret', max_length=75, blank=True, null=True)
    punchoutmode = models.CharField(db_column='PunchoutMode', max_length=50, blank=True, null=True)
    punchoutcert = models.CharField(db_column='PunchoutCert', max_length=50, blank=True, null=True)
    punchoutcustdomain = models.CharField(db_column='PunchoutCustDomain', max_length=50, blank=True, null=True)
    punchoutdebug = models.IntegerField(db_column='PunchoutDebug', blank=True, null=True)
    punchoutencode = models.IntegerField(db_column='PunchoutEncode', blank=True, null=True)
    punchoutencodeurl = models.IntegerField(db_column='PunchoutEncodeURL', blank=True, null=True)
    backfill = models.IntegerField(db_column='Backfill')
    formularyrestricteditall = models.IntegerField(db_column='FormularyRestrictEditAll')
    relayforward = models.IntegerField(db_column='RelayForward')
    privateemail = models.IntegerField(db_column='PrivateEmail')
    usestrictlinenumbers = models.IntegerField(db_column='UseStrictLineNumbers')
    vmi = models.IntegerField(db_column='VMI')
    shiptoaddresschangenotify = models.IntegerField(db_column='ShipToAddressChangeNotify')
    allowlinenotes = models.IntegerField(db_column='AllowLineNotes')
    returnacknowledgment = models.IntegerField(db_column='ReturnAcknowledgment')
    acknowledgefromformulary = models.IntegerField(db_column='AcknowledgeFromFormulary')
    isa_link = models.CharField(db_column='ISA_Link', max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'Distributor'

    def __str__(self):
        return f'{str(self.distributor)} {self.long_desc}'
