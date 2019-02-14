# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class Distributor(models.Model):
#     portal_id = models.BigIntegerField()
#     distributor_id = models.BigAutoField(primary_key=True)
#     gln = models.CharField(db_column='GLN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     short_desc = models.CharField(max_length=60, blank=True, null=True)
#     long_desc = models.CharField(max_length=255, blank=True, null=True)
#     comm_queue = models.CharField(max_length=128, blank=True, null=True)
#     autoacknowledge = models.IntegerField(db_column='AutoAcknowledge')  # Field name made lowercase.
#     webaddress = models.CharField(max_length=255, blank=True, null=True)
#     webext = models.CharField(max_length=3, blank=True, null=True)
#     passcode = models.CharField(db_column='PassCode', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     pmtattnto = models.CharField(db_column='PmtAttnTo', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     pmtaddress = models.CharField(db_column='PmtAddress', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     pmtcity = models.CharField(db_column='PmtCity', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     pmtstateprov = models.CharField(db_column='PmtStateProv', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     pmtpostalcode = models.CharField(db_column='PmtPostalCode', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     pmtphone = models.CharField(db_column='PmtPhone', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     pmtfax = models.CharField(db_column='PmtFax', max_length=24, blank=True, null=True)  # Field name made lowercase.
#     pmtlogo = models.CharField(db_column='PmtLogo', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     pmttermsconditions = models.TextField(db_column='PmtTermsConditions', blank=True, null=True)  # Field name made lowercase.
#     pmtinvoiceinfo = models.TextField(db_column='PmtInvoiceInfo', blank=True, null=True)  # Field name made lowercase.
#     pmtinvoicelegal = models.TextField(db_column='PmtInvoiceLegal', blank=True, null=True)  # Field name made lowercase.
#     privatelabel = models.IntegerField(db_column='PrivateLabel', blank=True, null=True)  # Field name made lowercase.
#     privatelabellogo = models.CharField(db_column='PrivateLabelLogo', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     privatelabelsalesurl = models.CharField(db_column='PrivateLabelSalesURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     privatelabelsupporturl = models.CharField(db_column='PrivateLabelSupportURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     privatelabelemailfrom = models.CharField(db_column='PrivateLabelEmailFrom', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     privatelabelemailheader = models.TextField(db_column='PrivateLabelEmailHeader', blank=True, null=True)  # Field name made lowercase.
#     privatelabelemailfooter = models.TextField(db_column='PrivateLabelEmailFooter', blank=True, null=True)  # Field name made lowercase.
#     punchoutenabled = models.IntegerField(db_column='PunchoutEnabled', blank=True, null=True)  # Field name made lowercase.
#     punchouturl = models.CharField(db_column='PunchoutURL', max_length=125, blank=True, null=True)  # Field name made lowercase.
#     punchoutsecret = models.CharField(db_column='PunchoutSecret', max_length=75, blank=True, null=True)  # Field name made lowercase.
#     punchoutmode = models.CharField(db_column='PunchoutMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     punchoutcert = models.CharField(db_column='PunchoutCert', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     punchoutcustdomain = models.CharField(db_column='PunchoutCustDomain', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     punchoutdebug = models.IntegerField(db_column='PunchoutDebug', blank=True, null=True)  # Field name made lowercase.
#     punchoutencode = models.IntegerField(db_column='PunchoutEncode', blank=True, null=True)  # Field name made lowercase.
#     punchoutencodeurl = models.IntegerField(db_column='PunchoutEncodeURL', blank=True, null=True)  # Field name made lowercase.
#     backfill = models.IntegerField(db_column='Backfill')  # Field name made lowercase.
#     formularyrestricteditall = models.IntegerField(db_column='FormularyRestrictEditAll')  # Field name made lowercase.
#     relayforward = models.IntegerField(db_column='RelayForward')  # Field name made lowercase.
#     privateemail = models.IntegerField(db_column='PrivateEmail')  # Field name made lowercase.
#     usestrictlinenumbers = models.IntegerField(db_column='UseStrictLineNumbers')  # Field name made lowercase.
#     vmi = models.IntegerField(db_column='VMI')  # Field name made lowercase.
#     shiptoaddresschangenotify = models.IntegerField(db_column='ShipToAddressChangeNotify')  # Field name made lowercase.
#     allowlinenotes = models.IntegerField(db_column='AllowLineNotes')  # Field name made lowercase.
#     returnacknowledgment = models.IntegerField(db_column='ReturnAcknowledgment')  # Field name made lowercase.
#     acknowledgefromformulary = models.IntegerField(db_column='AcknowledgeFromFormulary')  # Field name made lowercase.
#     isa_link = models.CharField(db_column='ISA_Link', max_length=15, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'distributor'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class IdApplication(models.Model):
#     applicationid = models.CharField(db_column='ApplicationID', primary_key=True, max_length=12)  # Field name made lowercase.
#     industryid = models.CharField(db_column='IndustryID', max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
#     lastupdatedate = models.DateField(db_column='LastUpdateDate')  # Field name made lowercase.
#     lastupdatetime = models.TimeField(db_column='LastUpdateTime')  # Field name made lowercase.
#     installedversionnumber = models.CharField(db_column='InstalledVersionNumber', max_length=24)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_application'
#         unique_together = (('applicationid', 'industryid'), ('applicationid', 'industryid'),)


# class IdBillingMethod(models.Model):
#     billingmethod = models.CharField(db_column='BillingMethod', primary_key=True, max_length=60)  # Field name made lowercase.
#     billingdescription = models.CharField(db_column='BillingDescription', max_length=240)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_billing_method'


# class IdBusiness(models.Model):
#     business_id = models.BigAutoField(primary_key=True)
#     businessshortname = models.CharField(db_column='BusinessShortName', max_length=24)  # Field name made lowercase.
#     businessname = models.CharField(db_column='BusinessName', max_length=60)  # Field name made lowercase.
#     legalname = models.CharField(db_column='LegalName', max_length=60)  # Field name made lowercase.
#     taxidnumber = models.CharField(db_column='TaxIDNumber', max_length=10)  # Field name made lowercase.
#     dunnandbradstreetnumber = models.CharField(db_column='DunnAndBradstreetNumber', max_length=60)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=60)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=60)  # Field name made lowercase.
#     address3 = models.CharField(db_column='Address3', max_length=60)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=60)  # Field name made lowercase.
#     stateprov = models.CharField(db_column='StateProv', max_length=4)  # Field name made lowercase.
#     postalcode = models.CharField(db_column='PostalCode', max_length=10)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=60)  # Field name made lowercase.
#     telephone = models.CharField(db_column='Telephone', max_length=12)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=12)  # Field name made lowercase.
#     weburl = models.CharField(db_column='WebURL', max_length=60)  # Field name made lowercase.
#     queuebase = models.CharField(db_column='QueueBase', max_length=128)  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
#     gln = models.CharField(db_column='GLN', max_length=13, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_business'


# class IdBusinessRelation(models.Model):
#     business_id = models.BigIntegerField(primary_key=True)
#     businessshortname = models.CharField(db_column='BusinessShortName', max_length=24)  # Field name made lowercase.
#     relationid = models.CharField(db_column='RelationID', max_length=24)  # Field name made lowercase.
#     relationtypeid = models.CharField(db_column='RelationTypeID', max_length=12)  # Field name made lowercase.
#     relationreference = models.CharField(db_column='RelationReference', max_length=24)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_business_relation'
#         unique_together = (('business_id', 'relationid', 'relationtypeid'),)


# class IdBusinessRules(models.Model):
#     ruleid = models.CharField(db_column='RuleID', primary_key=True, max_length=60)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
#     rule = models.TextField(db_column='Rule')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_business_rules'


# class IdCommError(models.Model):
#     commlogid = models.BigIntegerField(db_column='CommLogID', primary_key=True)  # Field name made lowercase.
#     commlogerrorid = models.BigAutoField(db_column='CommLogErrorID')  # Field name made lowercase.
#     errorcode = models.CharField(db_column='ErrorCode', max_length=255)  # Field name made lowercase.
#     transxml = models.TextField(db_column='TransXML')  # Field name made lowercase.
#     transsql = models.TextField(db_column='TransSQL')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_comm_error'
#         unique_together = (('commlogid', 'commlogerrorid'),)


# class IdCommLog(models.Model):
#     commlogid = models.BigAutoField(db_column='CommLogID', primary_key=True)  # Field name made lowercase.
#     commdate = models.DateField(db_column='CommDate')  # Field name made lowercase.
#     commtime = models.TimeField(db_column='CommTime')  # Field name made lowercase.
#     commdestination = models.CharField(db_column='CommDestination', max_length=255)  # Field name made lowercase.
#     incoming = models.PositiveIntegerField(db_column='Incoming')  # Field name made lowercase.
#     outgoing = models.PositiveIntegerField(db_column='Outgoing')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_comm_log'


# class IdCommTransIn(models.Model):
#     commlogid = models.BigIntegerField(db_column='CommLogID', primary_key=True)  # Field name made lowercase.
#     translogid = models.BigIntegerField(db_column='TransLogID')  # Field name made lowercase.
#     transxml = models.TextField(db_column='TransXML')  # Field name made lowercase.
#     transsql = models.TextField(db_column='TransSQL')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_comm_trans_in'
#         unique_together = (('commlogid', 'translogid'),)


# class IdCommTransOut(models.Model):
#     commlogid = models.BigIntegerField(db_column='CommLogID', primary_key=True)  # Field name made lowercase.
#     translogid = models.BigIntegerField(db_column='TransLogID')  # Field name made lowercase.
#     transxml = models.TextField(db_column='TransXML')  # Field name made lowercase.
#     transsql = models.TextField(db_column='TransSQL')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_comm_trans_out'
#         unique_together = (('commlogid', 'translogid'),)


# class IdErrors(models.Model):
#     errorid = models.CharField(db_column='ErrorID', primary_key=True, max_length=12)  # Field name made lowercase.
#     language = models.CharField(db_column='Language', max_length=5)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_errors'
#         unique_together = (('errorid', 'language'),)


# class IdEventNotify(models.Model):
#     eventnum = models.PositiveSmallIntegerField(db_column='EventNum', primary_key=True)  # Field name made lowercase.
#     eventid = models.CharField(db_column='EventID', max_length=60)  # Field name made lowercase.
#     severity = models.IntegerField(db_column='Severity')  # Field name made lowercase.
#     message = models.CharField(db_column='Message', max_length=255)  # Field name made lowercase.
#     messagequeue = models.CharField(db_column='MessageQueue', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_event_notify'


# class IdFaccodes(models.Model):
#     faccode_id = models.AutoField(primary_key=True)
#     faccodedescription = models.CharField(db_column='FaccodeDescription', max_length=50)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_faccodes'


# class IdFileVersions(models.Model):
#     filename = models.CharField(db_column='Filename', max_length=255)  # Field name made lowercase.
#     versionnum = models.CharField(db_column='VersionNum', max_length=50)  # Field name made lowercase.
#     versiondate = models.DateTimeField(db_column='VersionDate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_file_versions'


# class IdFormatFields(models.Model):
#     formatname = models.CharField(db_column='FormatName', primary_key=True, max_length=60)  # Field name made lowercase.
#     line = models.CharField(db_column='Line', max_length=60)  # Field name made lowercase.
#     fieldname = models.CharField(db_column='FieldName', max_length=60)  # Field name made lowercase.
#     sequence = models.PositiveIntegerField(db_column='Sequence')  # Field name made lowercase.
#     start = models.PositiveIntegerField(db_column='Start')  # Field name made lowercase.
#     length = models.PositiveIntegerField(db_column='Length')  # Field name made lowercase.
#     maxlength = models.PositiveIntegerField(db_column='MaxLength')  # Field name made lowercase.
#     fieldqualifier = models.CharField(db_column='FieldQualifier', max_length=24)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=3)  # Field name made lowercase.
#     format = models.CharField(db_column='Format', max_length=120)  # Field name made lowercase.
#     justification = models.CharField(db_column='Justification', max_length=1)  # Field name made lowercase.
#     defaultvalue = models.CharField(db_column='DefaultValue', max_length=60)  # Field name made lowercase.
#     trim = models.PositiveIntegerField(db_column='Trim')  # Field name made lowercase.
#     required = models.IntegerField(db_column='Required')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_format_fields'
#         unique_together = (('formatname', 'line', 'fieldname'),)


# class IdFormatLayout(models.Model):
#     formatname = models.CharField(db_column='FormatName', primary_key=True, max_length=60)  # Field name made lowercase.
#     parent = models.CharField(db_column='Parent', max_length=60)  # Field name made lowercase.
#     line = models.CharField(db_column='Line', max_length=60)  # Field name made lowercase.
#     sequence = models.PositiveIntegerField(db_column='Sequence')  # Field name made lowercase.
#     required = models.PositiveIntegerField(db_column='Required')  # Field name made lowercase.
#     minoccurance = models.PositiveIntegerField(db_column='MinOccurance')  # Field name made lowercase.
#     maxoccurance = models.IntegerField(db_column='MaxOccurance')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_format_layout'
#         unique_together = (('formatname', 'parent', 'line'),)


# class IdFormatLines(models.Model):
#     formatname = models.CharField(db_column='FormatName', primary_key=True, max_length=60)  # Field name made lowercase.
#     line = models.CharField(db_column='Line', max_length=60)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=3)  # Field name made lowercase.
#     fielddelimiter = models.CharField(db_column='FieldDelimiter', max_length=24)  # Field name made lowercase.
#     linedelimiter = models.CharField(db_column='LineDelimiter', max_length=24)  # Field name made lowercase.
#     lineidentifier = models.CharField(db_column='LineIdentifier', max_length=60)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_format_lines'
#         unique_together = (('formatname', 'line'),)


# class IdFormatRelation(models.Model):
#     formatname = models.CharField(db_column='FormatName', primary_key=True, max_length=60)  # Field name made lowercase.
#     parent = models.CharField(db_column='Parent', max_length=60)  # Field name made lowercase.
#     seq = models.PositiveIntegerField(db_column='Seq')  # Field name made lowercase.
#     child = models.CharField(db_column='Child', max_length=60)  # Field name made lowercase.
#     parentkey = models.CharField(db_column='ParentKey', max_length=60)  # Field name made lowercase.
#     childkey = models.CharField(db_column='ChildKey', max_length=60)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_format_relation'
#         unique_together = (('formatname', 'parent', 'seq'), ('formatname', 'parent', 'child', 'childkey'),)


# class IdGroup(models.Model):
#     groupid = models.CharField(db_column='GroupID', primary_key=True, max_length=12)  # Field name made lowercase.
#     groupdescription = models.CharField(db_column='GroupDescription', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_group'


# class IdGroupValidate(models.Model):
#     groupid = models.CharField(db_column='GroupID', primary_key=True, max_length=12)  # Field name made lowercase.
#     valueid = models.CharField(db_column='ValueID', max_length=12)  # Field name made lowercase.
#     value = models.CharField(db_column='Value', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_group_validate'
#         unique_together = (('groupid', 'valueid'),)


# class IdHcmCharges(models.Model):
#     transid = models.AutoField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     business_id = models.BigIntegerField()
#     transdate = models.DateField(db_column='TransDate')  # Field name made lowercase.
#     transtime = models.TimeField(db_column='TransTime')  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12)  # Field name made lowercase.
#     patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
#     fromrecurtransid = models.PositiveIntegerField(db_column='FromRecurTransID')  # Field name made lowercase.
#     billingmethod = models.CharField(db_column='BillingMethod', max_length=60)  # Field name made lowercase.
#     exported = models.IntegerField(db_column='Exported')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_charges'


# class IdHcmChargesOther(models.Model):
#     transid = models.PositiveIntegerField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.PositiveIntegerField(db_column='LineNum')  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     quantity = models.DecimalField(db_column='Quantity', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     unitid = models.CharField(db_column='UnitID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_charges_other'
#         unique_together = (('transid', 'linenum'),)


# class IdHcmChargesSupply(models.Model):
#     transid = models.PositiveIntegerField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     linetype = models.CharField(db_column='LineType', max_length=2)  # Field name made lowercase.
#     parentlinenum = models.PositiveIntegerField(db_column='ParentLineNum')  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     product_num = models.BigIntegerField()
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     distributor_id = models.BigIntegerField()
#     quantity = models.DecimalField(db_column='Quantity', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     unitid = models.CharField(db_column='UnitID', max_length=12)  # Field name made lowercase.
#     amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=4)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_charges_supply'
#         unique_together = (('transid', 'linenum'),)


# class IdHcmOrder(models.Model):
#     transid = models.AutoField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     transdate = models.DateField(db_column='TransDate')  # Field name made lowercase.
#     transtime = models.TimeField(db_column='TransTime')  # Field name made lowercase.
#     businessid = models.BigIntegerField(db_column='BusinessID')  # Field name made lowercase.
#     supplierid = models.BigIntegerField(db_column='SupplierID')  # Field name made lowercase.
#     requestdate = models.DateField(db_column='RequestDate')  # Field name made lowercase.
#     transreference = models.CharField(db_column='TransReference', max_length=24)  # Field name made lowercase.
#     externaltransnum = models.CharField(db_column='ExternalTransNum', max_length=24)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12)  # Field name made lowercase.
#     ordered = models.PositiveIntegerField(db_column='Ordered')  # Field name made lowercase.
#     ordereddate = models.DateField(db_column='OrderedDate')  # Field name made lowercase.
#     orderedtime = models.TimeField(db_column='OrderedTime')  # Field name made lowercase.
#     received = models.PositiveIntegerField(db_column='Received')  # Field name made lowercase.
#     closed = models.PositiveIntegerField(db_column='Closed')  # Field name made lowercase.
#     confirmed = models.PositiveIntegerField(db_column='Confirmed')  # Field name made lowercase.
#     confirmdate = models.DateField(db_column='ConfirmDate')  # Field name made lowercase.
#     confirmtime = models.TimeField(db_column='ConfirmTime')  # Field name made lowercase.
#     approved = models.PositiveIntegerField(db_column='Approved')  # Field name made lowercase.
#     approveddate = models.DateField(db_column='ApprovedDate')  # Field name made lowercase.
#     approvedtime = models.TimeField(db_column='ApprovedTime')  # Field name made lowercase.
#     approveduserid = models.CharField(db_column='ApprovedUserID', max_length=12)  # Field name made lowercase.
#     notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_order'


# class IdHcmOrderLabels(models.Model):
#     transid = models.PositiveIntegerField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     orderqty = models.DecimalField(db_column='OrderQty', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     orderunitid = models.CharField(db_column='OrderUnitID', max_length=12)  # Field name made lowercase.
#     dispenseunitid = models.CharField(db_column='DispenseUnitID', max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=65)  # Field name made lowercase.
#     numberoflabels = models.PositiveIntegerField(db_column='NumberOfLabels')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_order_labels'
#         unique_together = (('transid', 'linenum'),)


# class IdHcmOrderLines(models.Model):
#     transid = models.PositiveIntegerField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     product_num = models.BigIntegerField()
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     recommendqty = models.DecimalField(db_column='RecommendQty', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     recommendunitid = models.CharField(db_column='RecommendUnitID', max_length=12)  # Field name made lowercase.
#     orderqty = models.DecimalField(db_column='OrderQty', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     orderunitid = models.CharField(db_column='OrderUnitID', max_length=12)  # Field name made lowercase.
#     receivedqty = models.DecimalField(db_column='ReceivedQty', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     previousreceivedqty = models.DecimalField(db_column='PreviousReceivedQty', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     receivedunitid = models.CharField(db_column='ReceivedUnitID', max_length=12)  # Field name made lowercase.
#     receiveddate = models.DateField(db_column='ReceivedDate')  # Field name made lowercase.
#     receivedtime = models.TimeField(db_column='ReceivedTime')  # Field name made lowercase.
#     closed = models.PositiveIntegerField(db_column='Closed')  # Field name made lowercase.
#     confirmed = models.PositiveIntegerField(db_column='Confirmed')  # Field name made lowercase.
#     confirmdate = models.DateField(db_column='ConfirmDate')  # Field name made lowercase.
#     confirmtime = models.TimeField(db_column='ConfirmTime')  # Field name made lowercase.
#     extendedcost = models.DecimalField(db_column='ExtendedCost', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     costunitid = models.CharField(db_column='CostUnitID', max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=120)  # Field name made lowercase.
#     unitcost = models.DecimalField(db_column='UnitCost', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     specialorder = models.PositiveIntegerField(db_column='SpecialOrder')  # Field name made lowercase.
#     receivedunitcost = models.DecimalField(db_column='ReceivedUnitCost', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     receivedextendedcost = models.DecimalField(db_column='ReceivedExtendedCost', max_digits=12, decimal_places=4)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_order_lines'
#         unique_together = (('transid', 'linenum'),)


# class IdHcmOrderLink(models.Model):
#     potransid = models.PositiveIntegerField(db_column='POTransID', primary_key=True)  # Field name made lowercase.
#     polinenum = models.PositiveIntegerField(db_column='POLineNum')  # Field name made lowercase.
#     sotransnum = models.PositiveIntegerField(db_column='SOTransNum')  # Field name made lowercase.
#     solinenum = models.PositiveIntegerField(db_column='SOLineNum')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_order_link'
#         unique_together = (('potransid', 'polinenum', 'sotransnum', 'solinenum'),)


# class IdHcmOrderRec(models.Model):
#     transid = models.AutoField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     transdate = models.DateField(db_column='TransDate')  # Field name made lowercase.
#     transtime = models.TimeField(db_column='TransTime')  # Field name made lowercase.
#     potransid = models.PositiveIntegerField(db_column='POTransID')  # Field name made lowercase.
#     invoicematched = models.PositiveIntegerField(db_column='InvoiceMatched')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_order_rec'


# class IdHcmOrderRecLines(models.Model):
#     transid = models.PositiveIntegerField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     ordertransid = models.PositiveIntegerField(db_column='OrderTransID')  # Field name made lowercase.
#     orderlinenum = models.PositiveIntegerField(db_column='OrderLineNum')  # Field name made lowercase.
#     receivedqty = models.DecimalField(db_column='ReceivedQty', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     receivedunitid = models.CharField(db_column='ReceivedUnitID', max_length=12)  # Field name made lowercase.
#     updatedunitcost = models.DecimalField(db_column='UpdatedUnitCost', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_order_rec_lines'
#         unique_together = (('transid', 'linenum'),)


# class IdHcmPersonAttr(models.Model):
#     personid = models.PositiveIntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     medicalrecordid = models.CharField(db_column='MedicalRecordID', max_length=60)  # Field name made lowercase.
#     admitdate = models.DateField(db_column='AdmitDate')  # Field name made lowercase.
#     dischargedate = models.DateField(db_column='DischargeDate', blank=True, null=True)  # Field name made lowercase.
#     billingmethod = models.CharField(db_column='BillingMethod', max_length=60)  # Field name made lowercase.
#     payor = models.CharField(db_column='Payor', max_length=120)  # Field name made lowercase.
#     insuranceid = models.CharField(db_column='InsuranceID', max_length=60)  # Field name made lowercase.
#     medicareid = models.CharField(db_column='MedicareID', max_length=60)  # Field name made lowercase.
#     medicaidid = models.CharField(db_column='MedicaidID', max_length=60)  # Field name made lowercase.
#     facilityid = models.CharField(db_column='FacilityID', max_length=12)  # Field name made lowercase.
#     locationdescription = models.CharField(db_column='LocationDescription', max_length=60)  # Field name made lowercase.
#     room = models.CharField(db_column='Room', max_length=60)  # Field name made lowercase.
#     bed = models.CharField(db_column='Bed', max_length=60)  # Field name made lowercase.
#     pricegroup = models.CharField(db_column='PriceGroup', max_length=60)  # Field name made lowercase.
#     level = models.CharField(db_column='Level', max_length=12)  # Field name made lowercase.
#     incontinencesize = models.CharField(db_column='IncontinenceSize', max_length=25)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_person_attr'


# class IdHcmPersonBillingMethod(models.Model):
#     personid = models.PositiveIntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     begindate = models.DateField(db_column='BeginDate')  # Field name made lowercase.
#     enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
#     billingmethod = models.CharField(db_column='BillingMethod', max_length=60)  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_person_billing_method'
#         unique_together = (('personid', 'begindate', 'enddate', 'active'),)


# class IdHcmProductTemporary(models.Model):
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_product_temporary'


# class IdHcmScanLog(models.Model):
#     scanid = models.AutoField(db_column='ScanID', primary_key=True)  # Field name made lowercase.
#     source = models.CharField(db_column='Source', max_length=10)  # Field name made lowercase.
#     rawscans = models.TextField(db_column='RawScans')  # Field name made lowercase.
#     scanuser = models.CharField(db_column='ScanUser', max_length=50)  # Field name made lowercase.
#     syncdatetime = models.DateTimeField(db_column='SyncDateTime')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_scan_log'


# class IdHcmVendorAttr(models.Model):
#     vendorattrid = models.AutoField(db_column='VendorAttrID', primary_key=True)  # Field name made lowercase.
#     vendorid = models.CharField(db_column='VendorID', max_length=24)  # Field name made lowercase.
#     portaldistributorid = models.PositiveIntegerField(db_column='PortalDistributorID')  # Field name made lowercase.
#     vendorisprimary = models.PositiveIntegerField(db_column='VendorIsPrimary')  # Field name made lowercase.
#     queueorder = models.CharField(db_column='QueueOrder', max_length=160)  # Field name made lowercase.
#     queueorderconfirm = models.CharField(db_column='QueueOrderConfirm', max_length=160)  # Field name made lowercase.
#     notifyemail = models.CharField(db_column='NotifyEmail', max_length=160)  # Field name made lowercase.
#     notifyemailcc = models.CharField(db_column='NotifyEmailCC', max_length=160)  # Field name made lowercase.
#     gln = models.CharField(db_column='GLN', max_length=13, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_hcm_vendor_attr'


# class IdIndustry(models.Model):
#     industryid = models.CharField(db_column='IndustryID', primary_key=True, max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
#     siccode = models.PositiveIntegerField(db_column='SICCode')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_industry'


# class IdInventoryTransfer(models.Model):
#     transid = models.AutoField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     transdatetime = models.DateTimeField(db_column='TransDateTime')  # Field name made lowercase.
#     businessid = models.CharField(db_column='BusinessID', max_length=24)  # Field name made lowercase.
#     facilityid = models.CharField(db_column='FacilityID', max_length=24)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=24)  # Field name made lowercase.
#     fromlocationid = models.CharField(db_column='FromLocationID', max_length=24)  # Field name made lowercase.
#     tolocationid = models.CharField(db_column='ToLocationID', max_length=24)  # Field name made lowercase.
#     transferdatetime = models.DateTimeField(db_column='TransferDateTime')  # Field name made lowercase.
#     transferuserid = models.CharField(db_column='TransferUserID', max_length=24)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=4)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_inventory_transfer'


# class IdInventoryTransferLines(models.Model):
#     transid = models.PositiveIntegerField(db_column='TransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=24)  # Field name made lowercase.
#     fromqty = models.DecimalField(db_column='FromQty', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     fromunitid = models.CharField(db_column='FromUnitID', max_length=12)  # Field name made lowercase.
#     toqty = models.DecimalField(db_column='ToQty', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     tounitid = models.CharField(db_column='ToUnitID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_inventory_transfer_lines'
#         unique_together = (('transid', 'linenum'),)


# class IdLinks(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     link_sequence = models.PositiveSmallIntegerField(db_column='Link_Sequence')  # Field name made lowercase.
#     link_url = models.CharField(db_column='Link_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     link_name = models.CharField(db_column='Link_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_links'
#         unique_together = (('userid', 'link_sequence'),)


# class IdLocation(models.Model):
#     businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=24)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     locationdescription = models.CharField(db_column='LocationDescription', max_length=255)  # Field name made lowercase.
#     replenlocationid = models.CharField(db_column='ReplenLocationID', max_length=24)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_location'
#         unique_together = (('businessid', 'locationid'),)


# class IdMap(models.Model):
#     mapid = models.AutoField(db_column='MapID', primary_key=True)  # Field name made lowercase.
#     mappingname = models.CharField(db_column='MappingName', max_length=60)  # Field name made lowercase.
#     codexref = models.CharField(db_column='CodeXRef', max_length=60)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=12)  # Field name made lowercase.
#     formatname = models.CharField(db_column='FormatName', max_length=60)  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
#     consolidate = models.PositiveIntegerField(db_column='Consolidate', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_map'


# class IdMapXref(models.Model):
#     mapxrefname = models.CharField(db_column='MapXrefName', primary_key=True, max_length=40)  # Field name made lowercase.
#     valuefrom = models.CharField(db_column='ValueFrom', max_length=40)  # Field name made lowercase.
#     valueto = models.CharField(db_column='ValueTo', max_length=40)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_map_xref'
#         unique_together = (('mapxrefname', 'valuefrom'),)


# class IdMapping(models.Model):
#     mappingname = models.CharField(db_column='MappingName', primary_key=True, max_length=40)  # Field name made lowercase.
#     sourcename = models.CharField(db_column='SourceName', max_length=40)  # Field name made lowercase.
#     sourcefield = models.CharField(db_column='SourceField', max_length=40)  # Field name made lowercase.
#     conditionalname = models.CharField(db_column='ConditionalName', max_length=40)  # Field name made lowercase.
#     conditionalfield = models.CharField(db_column='ConditionalField', max_length=40)  # Field name made lowercase.
#     conditionalvalue = models.CharField(db_column='ConditionalValue', max_length=40)  # Field name made lowercase.
#     destinationname = models.CharField(db_column='DestinationName', max_length=40)  # Field name made lowercase.
#     destinationfield = models.CharField(db_column='DestinationField', max_length=40)  # Field name made lowercase.
#     mapping = models.CharField(db_column='Mapping', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     mappingtype = models.CharField(db_column='MappingType', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     conditionaltype = models.CharField(db_column='ConditionalType', max_length=40)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_mapping'
#         unique_together = (('mappingname', 'sourcefield', 'sourcename', 'destinationfield', 'destinationname', 'conditionalname', 'conditionalfield', 'conditionalvalue'),)


# class IdOptions(models.Model):
#     optionid = models.AutoField(db_column='OptionID', primary_key=True)  # Field name made lowercase.
#     optiondescription = models.CharField(db_column='OptionDescription', max_length=120)  # Field name made lowercase.
#     optionvalue = models.CharField(db_column='OptionValue', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_options'


# class IdPalmLinks(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     link_sequence = models.PositiveSmallIntegerField(db_column='Link_Sequence')  # Field name made lowercase.
#     link_url = models.CharField(db_column='Link_URL', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     link_name = models.CharField(db_column='Link_Name', max_length=60, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_palm_links'
#         unique_together = (('userid', 'link_sequence'),)


# class IdPerson(models.Model):
#     personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     ssnumber = models.CharField(db_column='SSNumber', max_length=11)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=60)  # Field name made lowercase.
#     middleinitial = models.CharField(db_column='MiddleInitial', max_length=1)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=60)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=60)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=60)  # Field name made lowercase.
#     address3 = models.CharField(db_column='Address3', max_length=60)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=60)  # Field name made lowercase.
#     stateprov = models.CharField(db_column='StateProv', max_length=4)  # Field name made lowercase.
#     postalcode = models.CharField(db_column='PostalCode', max_length=10)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=60)  # Field name made lowercase.
#     userlanguage = models.CharField(db_column='UserLanguage', max_length=60)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=60)  # Field name made lowercase.
#     telephone = models.CharField(db_column='Telephone', max_length=12)  # Field name made lowercase.
#     fax = models.CharField(db_column='Fax', max_length=12)  # Field name made lowercase.
#     cellphone = models.CharField(db_column='Cellphone', max_length=12)  # Field name made lowercase.
#     pager = models.CharField(db_column='Pager', max_length=12)  # Field name made lowercase.
#     pageremail = models.CharField(db_column='PagerEMail', max_length=60)  # Field name made lowercase.
#     wirelessemail = models.CharField(db_column='WirelessEMail', max_length=60)  # Field name made lowercase.
#     weburl = models.CharField(db_column='WebURL', max_length=60)  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
#     sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
#     race = models.CharField(db_column='Race', max_length=16)  # Field name made lowercase.
#     dateofbirth = models.DateField(db_column='DateOfBirth')  # Field name made lowercase.
#     age = models.PositiveIntegerField(db_column='Age')  # Field name made lowercase.
#     shipcode = models.IntegerField(db_column='ShipCode')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person'


# class IdPersonAddress(models.Model):
#     personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     addressid = models.CharField(db_column='AddressID', max_length=12)  # Field name made lowercase.
#     address1 = models.CharField(db_column='Address1', max_length=60)  # Field name made lowercase.
#     address2 = models.CharField(db_column='Address2', max_length=60)  # Field name made lowercase.
#     address3 = models.CharField(db_column='Address3', max_length=60)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=60)  # Field name made lowercase.
#     stateprov = models.CharField(db_column='StateProv', max_length=4)  # Field name made lowercase.
#     postalcode = models.CharField(db_column='PostalCode', max_length=10)  # Field name made lowercase.
#     country = models.CharField(db_column='Country', max_length=60)  # Field name made lowercase.
#     addressname = models.CharField(db_column='AddressName', max_length=60)  # Field name made lowercase.
#     addressnum = models.PositiveIntegerField(db_column='AddressNum')  # Field name made lowercase.
#     shipcode = models.IntegerField(db_column='ShipCode')  # Field name made lowercase.
#     attnfirstname = models.CharField(db_column='AttnFirstName', max_length=60)  # Field name made lowercase.
#     attnlastname = models.CharField(db_column='AttnLastName', max_length=60)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person_address'
#         unique_together = (('personid', 'addressid', 'addressnum'),)


# class IdPersonAttr(models.Model):
#     personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     attrid = models.CharField(db_column='AttrID', max_length=60)  # Field name made lowercase.
#     typeid = models.CharField(db_column='TypeID', max_length=2)  # Field name made lowercase.
#     attr_string = models.CharField(db_column='Attr_String', max_length=255)  # Field name made lowercase.
#     attr_int = models.IntegerField(db_column='Attr_Int')  # Field name made lowercase.
#     attr_float = models.FloatField(db_column='Attr_Float')  # Field name made lowercase.
#     attr_bool = models.IntegerField(db_column='Attr_Bool')  # Field name made lowercase.
#     attr_text = models.TextField(db_column='Attr_Text')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person_attr'
#         unique_together = (('personid', 'attrid'),)


# class IdPersonGroup(models.Model):
#     personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     groupid = models.CharField(db_column='GroupID', max_length=12)  # Field name made lowercase.
#     valueid = models.CharField(db_column='ValueID', max_length=12)  # Field name made lowercase.
#     groupvalue = models.CharField(db_column='GroupValue', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person_group'
#         unique_together = (('personid', 'groupid'),)


# class IdPersonProducts(models.Model):
#     personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     productreference = models.CharField(db_column='ProductReference', max_length=128)  # Field name made lowercase.
#     productdescription = models.CharField(db_column='ProductDescription', max_length=128)  # Field name made lowercase.
#     price = models.DecimalField(db_column='Price', max_digits=9, decimal_places=2)  # Field name made lowercase.
#     manufactured = models.PositiveIntegerField(db_column='Manufactured')  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
#     size = models.CharField(db_column='Size', max_length=25)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=25)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person_products'
#         unique_together = (('personid', 'productid'), ('personid', 'productid'),)


# class IdPersonRelation(models.Model):
#     personid = models.IntegerField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
#     relationid = models.IntegerField(db_column='RelationID')  # Field name made lowercase.
#     relationtypeid = models.CharField(db_column='RelationTypeID', max_length=12)  # Field name made lowercase.
#     relationreference = models.CharField(db_column='RelationReference', max_length=24)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person_relation'
#         unique_together = (('personid', 'relationid', 'relationtypeid'), ('personid', 'relationid', 'relationtypeid'),)


# class IdPersonTask(models.Model):
#     taskid = models.PositiveIntegerField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
#     personid = models.IntegerField(db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
#     assigneduserid = models.CharField(db_column='AssignedUserID', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     taskurl = models.CharField(db_column='TaskURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_person_task'


# class IdPortalPreferences(models.Model):
#     portalid = models.AutoField(db_column='PortalID', primary_key=True)  # Field name made lowercase.
#     portalname = models.CharField(db_column='PortalName', max_length=160)  # Field name made lowercase.
#     portalbaseurl = models.CharField(db_column='PortalBaseURL', max_length=160)  # Field name made lowercase.
#     portalusername = models.CharField(db_column='PortalUsername', max_length=160)  # Field name made lowercase.
#     portalpassword = models.CharField(db_column='PortalPassword', max_length=160)  # Field name made lowercase.
#     portalcustomerreference = models.CharField(db_column='PortalCustomerReference', max_length=60)  # Field name made lowercase.
#     portalprimaryvendor = models.CharField(db_column='PortalPrimaryVendor', max_length=60)  # Field name made lowercase.
#     lastproductupdatedatetime = models.DateTimeField(db_column='LastProductUpdateDateTime')  # Field name made lowercase.
#     supporturl = models.CharField(db_column='SupportURL', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_portal_preferences'


# class IdPriceGroup(models.Model):
#     businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=24)  # Field name made lowercase.
#     productpricecode = models.CharField(db_column='ProductPriceCode', max_length=24)  # Field name made lowercase.
#     personpricecode = models.CharField(db_column='PersonPriceCode', max_length=24)  # Field name made lowercase.
#     businesspricecode = models.CharField(db_column='BusinessPriceCode', max_length=24)  # Field name made lowercase.
#     priceamount = models.DecimalField(db_column='PriceAmount', max_digits=14, decimal_places=4)  # Field name made lowercase.
#     pricetype = models.CharField(db_column='PriceType', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_price_group'
#         unique_together = (('businessid', 'productpricecode', 'personpricecode', 'businesspricecode'),)


# class IdProduct(models.Model):
#     product_num = models.BigAutoField(primary_key=True)
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     business_id = models.BigIntegerField()
#     distributor_id = models.BigIntegerField()
#     manufacturer_id = models.BigIntegerField()
#     manufacturerpartnumber = models.CharField(db_column='ManufacturerPartNumber', max_length=120)  # Field name made lowercase.
#     primaryvendoritemnumber = models.CharField(db_column='PrimaryVendorItemNumber', max_length=120)  # Field name made lowercase.
#     internalitemnumber = models.CharField(db_column='InternalItemNumber', max_length=120)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
#     manufactured = models.PositiveIntegerField(db_column='Manufactured')  # Field name made lowercase.
#     kit = models.PositiveIntegerField(db_column='Kit')  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
#     perpetual = models.PositiveIntegerField(db_column='Perpetual')  # Field name made lowercase.
#     service = models.IntegerField(db_column='Service')  # Field name made lowercase.
#     size = models.CharField(db_column='Size', max_length=25)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=25)  # Field name made lowercase.
#     gtin = models.CharField(db_column='GTIN', max_length=14, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product'


# class IdProductAlias(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     alias = models.CharField(db_column='Alias', max_length=120)  # Field name made lowercase.
#     isbarcode = models.PositiveIntegerField(db_column='IsBarCode')  # Field name made lowercase.
#     isprintbarcode = models.PositiveIntegerField(db_column='IsPrintBarCode')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_alias'
#         unique_together = (('productid', 'alias'), ('productid', 'isprintbarcode', 'alias'),)


# class IdProductAttr(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     attrid = models.CharField(db_column='AttrID', max_length=60)  # Field name made lowercase.
#     typeid = models.CharField(db_column='TypeID', max_length=2)  # Field name made lowercase.
#     attr_string = models.CharField(db_column='Attr_String', max_length=255)  # Field name made lowercase.
#     attr_int = models.IntegerField(db_column='Attr_Int')  # Field name made lowercase.
#     attr_float = models.FloatField(db_column='Attr_Float')  # Field name made lowercase.
#     attr_bool = models.IntegerField(db_column='Attr_Bool')  # Field name made lowercase.
#     attr_text = models.TextField(db_column='Attr_Text', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_attr'
#         unique_together = (('productid', 'attrid'),)


# class IdProductCategories(models.Model):
#     categoryid = models.CharField(db_column='CategoryID', primary_key=True, max_length=60)  # Field name made lowercase.
#     categorydescription = models.CharField(db_column='CategoryDescription', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_categories'


# class IdProductChargeCodes(models.Model):
#     chargeid = models.CharField(db_column='ChargeID', primary_key=True, max_length=60)  # Field name made lowercase.
#     chargedescription = models.CharField(db_column='ChargeDescription', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_charge_codes'


# class IdProductCost(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     cost = models.DecimalField(db_column='Cost', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     costunitid = models.CharField(db_column='CostUnitID', max_length=12)  # Field name made lowercase.
#     effectivedate = models.DateField(db_column='EffectiveDate')  # Field name made lowercase.
#     contract = models.CharField(db_column='Contract', max_length=250)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_cost'
#         unique_together = (('productid', 'effectivedate'),)


# class IdProductGroup(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     groupid = models.CharField(db_column='GroupID', max_length=12)  # Field name made lowercase.
#     valueid = models.CharField(db_column='ValueID', max_length=120)  # Field name made lowercase.
#     groupvalue = models.CharField(db_column='GroupValue', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_group'
#         unique_together = (('productid', 'groupid'),)


# class IdProductKit(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     componentid = models.AutoField(db_column='ComponentID')  # Field name made lowercase.
#     componentproductid = models.CharField(db_column='ComponentProductID', max_length=60)  # Field name made lowercase.
#     componentqty = models.FloatField(db_column='ComponentQty')  # Field name made lowercase.
#     componentunitid = models.CharField(db_column='ComponentUnitID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_kit'
#         unique_together = (('productid', 'componentid'), ('productid', 'componentproductid'),)


# class IdProductPriceCodes(models.Model):
#     priceid = models.CharField(db_column='PriceID', primary_key=True, max_length=60)  # Field name made lowercase.
#     pricedescription = models.CharField(db_column='PriceDescription', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_price_codes'


# class IdProductQty(models.Model):
#     locationid = models.CharField(db_column='LocationID', primary_key=True, max_length=24)  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     qtytype = models.CharField(db_column='QtyType', max_length=60)  # Field name made lowercase.
#     quantity = models.DecimalField(db_column='Quantity', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     qtyuomid = models.CharField(db_column='QtyUOMID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_qty'
#         unique_together = (('locationid', 'productid', 'qtytype'),)


# class IdProductType(models.Model):
#     typeid = models.CharField(db_column='TypeID', primary_key=True, max_length=60)  # Field name made lowercase.
#     typedescription = models.CharField(db_column='TypeDescription', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_type'


# class IdProductTypeSize(models.Model):
#     typeid = models.CharField(db_column='TypeID', primary_key=True, max_length=60)  # Field name made lowercase.
#     sequence = models.PositiveIntegerField(db_column='Sequence')  # Field name made lowercase.
#     sizeid = models.CharField(db_column='SizeID', max_length=25)  # Field name made lowercase.
#     sizedescription = models.CharField(db_column='SizeDescription', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_type_size'
#         unique_together = (('typeid', 'sizeid'),)


# class IdProductUnit(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     unitid = models.CharField(db_column='UnitID', max_length=60)  # Field name made lowercase.
#     typeid = models.CharField(db_column='TypeID', max_length=16)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_unit'
#         unique_together = (('productid', 'unitid', 'typeid'),)


# class IdProductUnitConv(models.Model):
#     productid = models.CharField(db_column='ProductID', primary_key=True, max_length=60)  # Field name made lowercase.
#     unitid = models.CharField(db_column='UnitID', max_length=60)  # Field name made lowercase.
#     convqty = models.DecimalField(db_column='ConvQty', max_digits=20, decimal_places=8)  # Field name made lowercase.
#     convunitid = models.CharField(db_column='ConvUnitID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_unit_conv'
#         unique_together = (('productid', 'unitid', 'convunitid'),)


# class IdProductUsageImport(models.Model):
#     batchid = models.PositiveIntegerField(db_column='BatchID', primary_key=True)  # Field name made lowercase.
#     transid = models.AutoField(db_column='TransID')  # Field name made lowercase.
#     batchuserid = models.CharField(db_column='BatchUserID', max_length=12)  # Field name made lowercase.
#     batchdatetime = models.DateTimeField(db_column='BatchDateTime')  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     residentid = models.IntegerField(db_column='ResidentID')  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     unitid = models.CharField(db_column='UnitID', max_length=60)  # Field name made lowercase.
#     quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=0)  # Field name made lowercase.
#     exceptionid = models.CharField(db_column='ExceptionID', max_length=24)  # Field name made lowercase.
#     transdatetime = models.DateTimeField(db_column='TransDateTime')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_product_usage_import'
#         unique_together = (('batchid', 'transid'),)


# class IdPurchaseOrderTemp(models.Model):
#     vendorid = models.CharField(db_column='vendorID', max_length=60)  # Field name made lowercase.
#     productid = models.CharField(db_column='productID', max_length=60)  # Field name made lowercase.
#     quantity = models.FloatField()
#     unitid = models.CharField(db_column='unitID', max_length=60)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_purchase_order_temp'


# class IdQuestion(models.Model):
#     questionid = models.CharField(db_column='QuestionID', primary_key=True, max_length=64)  # Field name made lowercase.
#     seq = models.PositiveIntegerField(db_column='Seq')  # Field name made lowercase.
#     question = models.CharField(db_column='Question', max_length=128)  # Field name made lowercase.
#     answer = models.CharField(db_column='Answer', max_length=128)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=64)  # Field name made lowercase.
#     format = models.CharField(db_column='Format', max_length=64)  # Field name made lowercase.
#     parameter = models.CharField(db_column='Parameter', max_length=64)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_question'
#         unique_together = (('questionid', 'seq'),)


# class IdQueueType(models.Model):
#     queueid = models.CharField(db_column='QueueID', primary_key=True, max_length=12)  # Field name made lowercase.
#     queuebase = models.CharField(db_column='QueueBase', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=60, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_queue_type'


# class IdRecurCharges(models.Model):
#     recurtransid = models.AutoField(db_column='RecurTransID', primary_key=True)  # Field name made lowercase.
#     recurgroupid = models.PositiveIntegerField(db_column='RecurGroupID')  # Field name made lowercase.
#     businessid = models.CharField(db_column='BusinessID', max_length=24)  # Field name made lowercase.
#     facilityid = models.CharField(db_column='FacilityID', max_length=24)  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12)  # Field name made lowercase.
#     patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
#     recurcreatedate = models.DateTimeField(db_column='RecurCreateDate')  # Field name made lowercase.
#     recurstartdate = models.DateTimeField(db_column='RecurStartDate')  # Field name made lowercase.
#     recurenddate = models.DateTimeField(db_column='RecurEndDate')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_recur_charges'


# class IdRecurChargesSupply(models.Model):
#     recurtransid = models.PositiveIntegerField(db_column='RecurTransID', primary_key=True)  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=60)  # Field name made lowercase.
#     quantity = models.DecimalField(db_column='Quantity', max_digits=12, decimal_places=4)  # Field name made lowercase.
#     unitid = models.CharField(db_column='UnitID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_recur_charges_supply'
#         unique_together = (('recurtransid', 'linenum'),)


# class IdRecurGroup(models.Model):
#     recurgroupid = models.AutoField(db_column='RecurGroupID', primary_key=True)  # Field name made lowercase.
#     recurgroupdescription = models.CharField(db_column='RecurGroupDescription', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_recur_group'


# class IdRelationType(models.Model):
#     relationtypeid = models.CharField(db_column='RelationTypeID', primary_key=True, max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=60)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_relation_type'


# class IdReport(models.Model):
#     reportgroupid = models.CharField(db_column='ReportGroupID', primary_key=True, max_length=120)  # Field name made lowercase.
#     reportid = models.CharField(db_column='ReportID', max_length=120)  # Field name made lowercase.
#     reportdescription = models.CharField(db_column='ReportDescription', max_length=255)  # Field name made lowercase.
#     reportfilename = models.CharField(db_column='ReportFileName', max_length=255)  # Field name made lowercase.
#     reportodbcname = models.CharField(db_column='ReportODBCName', max_length=120)  # Field name made lowercase.
#     reportdbname = models.CharField(db_column='ReportDBName', max_length=120)  # Field name made lowercase.
#     reportdbuser = models.CharField(db_column='ReportDBUser', max_length=120)  # Field name made lowercase.
#     reportdbpassword = models.CharField(db_column='ReportDBPassword', max_length=120)  # Field name made lowercase.
#     lastrundate = models.DateField(db_column='LastRunDate')  # Field name made lowercase.
#     lastruntime = models.TimeField(db_column='LastRunTime')  # Field name made lowercase.
#     lastrunuserid = models.CharField(db_column='LastRunUserID', max_length=12)  # Field name made lowercase.
#     lastrunuser = models.CharField(db_column='LastRunUser', max_length=12)  # Field name made lowercase.
#     questionid = models.CharField(db_column='QuestionID', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     properties = models.CharField(db_column='Properties', max_length=128)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_report'
#         unique_together = (('reportgroupid', 'reportid'),)


# class IdReportGroup(models.Model):
#     reportgroupid = models.CharField(db_column='ReportGroupID', primary_key=True, max_length=120)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
#     directory = models.CharField(db_column='Directory', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_report_group'


# class IdSalesOrder(models.Model):
#     businessid = models.CharField(db_column='BusinessID', max_length=24)  # Field name made lowercase.
#     transtype = models.CharField(db_column='TransType', primary_key=True, max_length=8)  # Field name made lowercase.
#     transcode = models.CharField(db_column='TransCode', max_length=8)  # Field name made lowercase.
#     transnum = models.AutoField(db_column='TransNum')  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     transdate = models.DateField(db_column='TransDate')  # Field name made lowercase.
#     transamount = models.DecimalField(db_column='TransAmount', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12)  # Field name made lowercase.
#     custid = models.CharField(db_column='CustID', max_length=24)  # Field name made lowercase.
#     custshipid = models.CharField(db_column='CustShipID', max_length=24)  # Field name made lowercase.
#     custpo = models.CharField(db_column='CustPO', max_length=60)  # Field name made lowercase.
#     custrequestdate = models.DateField(db_column='CustRequestDate')  # Field name made lowercase.
#     externaltransid = models.CharField(db_column='ExternalTransID', max_length=60)  # Field name made lowercase.
#     comments = models.TextField(db_column='Comments')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_sales_order'
#         unique_together = (('transtype', 'transcode', 'transnum', 'businessid'),)


# class IdSalesOrderLines(models.Model):
#     businessid = models.CharField(db_column='BusinessID', primary_key=True, max_length=24)  # Field name made lowercase.
#     transtype = models.CharField(db_column='TransType', max_length=8)  # Field name made lowercase.
#     transcode = models.CharField(db_column='TransCode', max_length=8)  # Field name made lowercase.
#     transnum = models.PositiveIntegerField(db_column='TransNum')  # Field name made lowercase.
#     linenum = models.AutoField(db_column='LineNum')  # Field name made lowercase.
#     linetype = models.CharField(db_column='LineType', max_length=2)  # Field name made lowercase.
#     parentlinenum = models.PositiveIntegerField(db_column='ParentLineNum')  # Field name made lowercase.
#     locationid = models.CharField(db_column='LocationID', max_length=24)  # Field name made lowercase.
#     productid = models.CharField(db_column='ProductID', max_length=24)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=60)  # Field name made lowercase.
#     orderqty = models.DecimalField(db_column='OrderQty', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     orderunitid = models.CharField(db_column='OrderUnitID', max_length=12)  # Field name made lowercase.
#     unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     priceunitid = models.CharField(db_column='PriceUnitID', max_length=12)  # Field name made lowercase.
#     extendedprice = models.DecimalField(db_column='ExtendedPrice', max_digits=10, decimal_places=4)  # Field name made lowercase.
#     custshipid = models.CharField(db_column='CustShipID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_sales_order_lines'
#         unique_together = (('businessid', 'transtype', 'transcode', 'transnum', 'linenum'),)


# class IdServiceCode(models.Model):
#     servicecodegroup = models.CharField(db_column='ServiceCodeGroup', max_length=12)  # Field name made lowercase.
#     servicecodeid = models.CharField(db_column='ServiceCodeID', primary_key=True, max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_service_code'
#         unique_together = (('servicecodeid', 'servicecodegroup'),)


# class IdShipping(models.Model):
#     shipid = models.CharField(db_column='ShipID', primary_key=True, max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=60)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_shipping'


# class IdStatusCodes(models.Model):
#     statusid = models.CharField(db_column='StatusID', primary_key=True, max_length=12)  # Field name made lowercase.
#     statustype = models.CharField(db_column='StatusType', max_length=2)  # Field name made lowercase.
#     statusvalue = models.CharField(db_column='StatusValue', max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_status_codes'
#         unique_together = (('statusid', 'statustype', 'statusvalue'),)


# class IdTimeEntry(models.Model):
#     timeid = models.PositiveIntegerField(db_column='TimeID', primary_key=True)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12)  # Field name made lowercase.
#     timetypeid = models.CharField(db_column='TimeTypeID', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     businessid = models.CharField(db_column='BusinessID', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     begintime = models.TimeField(db_column='BeginTime', blank=True, null=True)  # Field name made lowercase.
#     endtime = models.TimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
#     departbusinessid = models.CharField(db_column='DepartBusinessID', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     destbusinessid = models.CharField(db_column='DestBusinessID', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     beginodometer = models.FloatField(db_column='BeginOdometer', blank=True, null=True)  # Field name made lowercase.
#     endodometer = models.FloatField(db_column='EndOdometer', blank=True, null=True)  # Field name made lowercase.
#     paidhours = models.FloatField(db_column='PaidHours', blank=True, null=True)  # Field name made lowercase.
#     partahours = models.FloatField(db_column='PartAHours', blank=True, null=True)  # Field name made lowercase.
#     partbhours = models.FloatField(db_column='PartBHours', blank=True, null=True)  # Field name made lowercase.
#     otherhours = models.FloatField(db_column='OtherHours', blank=True, null=True)  # Field name made lowercase.
#     transdate = models.DateField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
#     assocapproved = models.PositiveIntegerField(db_column='AssocApproved', blank=True, null=True)  # Field name made lowercase.
#     managerapproved = models.PositiveIntegerField(db_column='ManagerApproved', blank=True, null=True)  # Field name made lowercase.
#     forwardedtopayroll = models.PositiveIntegerField(db_column='ForwardedToPayroll', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_time_entry'
#         unique_together = (('timeid', 'userid'),)


# class IdTimeExplanation(models.Model):
#     timeexplainid = models.PositiveIntegerField(db_column='TimeExplainID', primary_key=True)  # Field name made lowercase.
#     userid = models.CharField(db_column='UserID', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     explanation = models.TextField(db_column='Explanation', blank=True, null=True)  # Field name made lowercase.
#     weekstarting = models.DateField(db_column='WeekStarting')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_time_explanation'


# class IdTrans(models.Model):
#     transnum = models.AutoField(db_column='TransNum', primary_key=True)  # Field name made lowercase.
#     transid = models.CharField(db_column='TransID', max_length=12)  # Field name made lowercase.
#     frombusinessid = models.CharField(db_column='FromBusinessID', max_length=24)  # Field name made lowercase.
#     tobusinessid = models.CharField(db_column='ToBusinessID', max_length=24)  # Field name made lowercase.
#     transdatetime = models.DateTimeField(db_column='TransDateTime')  # Field name made lowercase.
#     numlines = models.PositiveIntegerField(db_column='NumLines')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_trans'


# class IdTransLog(models.Model):
#     translogid = models.BigAutoField(db_column='TransLogID', primary_key=True)  # Field name made lowercase.
#     destination = models.CharField(db_column='Destination', max_length=255)  # Field name made lowercase.
#     transxml = models.TextField(db_column='TransXML')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_trans_log'


# class IdUnit(models.Model):
#     unitid = models.CharField(db_column='UnitID', primary_key=True, max_length=12)  # Field name made lowercase.
#     description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_unit'


# class IdUnitConv(models.Model):
#     unitid = models.CharField(db_column='UnitID', primary_key=True, max_length=60)  # Field name made lowercase.
#     convqty = models.DecimalField(db_column='ConvQty', max_digits=20, decimal_places=8)  # Field name made lowercase.
#     convunitid = models.CharField(db_column='ConvUnitID', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_unit_conv'


# class IdUser(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=120)  # Field name made lowercase.
#     personid = models.PositiveIntegerField(db_column='PersonID')  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=60)  # Field name made lowercase.
#     middleinitial = models.CharField(db_column='MiddleInitial', max_length=1)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=60)  # Field name made lowercase.
#     email = models.CharField(db_column='EMail', max_length=60)  # Field name made lowercase.
#     active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
#     usercategory = models.CharField(db_column='UserCategory', max_length=60)  # Field name made lowercase.
#     usersecuritylevel = models.PositiveIntegerField(db_column='UserSecurityLevel')  # Field name made lowercase.
#     accesscardid = models.TextField(db_column='AccessCardID', unique=True, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_user'


# class IdUserApplication(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     applicationid = models.CharField(db_column='ApplicationID', max_length=12)  # Field name made lowercase.
#     securitylevel = models.CharField(db_column='SecurityLevel', max_length=12)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_user_application'
#         unique_together = (('userid', 'applicationid'), ('userid', 'applicationid'),)


# class IdUserApplicationQueue(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     applicationid = models.CharField(db_column='ApplicationID', max_length=12)  # Field name made lowercase.
#     queueid = models.CharField(db_column='QueueID', max_length=12)  # Field name made lowercase.
#     queue = models.CharField(db_column='Queue', max_length=128)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_user_application_queue'
#         unique_together = (('userid', 'applicationid', 'queueid'), ('userid', 'applicationid', 'queueid'),)


# class IdUserIvStartPanel(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     sc_name = models.CharField(max_length=255)

#     class Meta:
#         managed = False
#         db_table = 'id_user_iv_start_panel'


# class IdUserReportGroup(models.Model):
#     userid = models.CharField(db_column='UserID', primary_key=True, max_length=12)  # Field name made lowercase.
#     reportgroupid = models.CharField(db_column='ReportGroupID', max_length=120)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'id_user_report_group'
#         unique_together = (('userid', 'reportgroupid'),)


# class Ints(models.Model):
#     i = models.IntegerField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'ints'


# class TempResident(models.Model):
#     resnum = models.CharField(max_length=50, blank=True, null=True)
#     lastname = models.CharField(max_length=50, blank=True, null=True)
#     firstname = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'temp_resident'
