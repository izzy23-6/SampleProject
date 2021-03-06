# Generated by Django 2.1.5 on 2019-01-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractPrice',
            fields=[
                ('contractprice_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('portal_id', models.BigIntegerField()),
                ('distributor_id', models.BigIntegerField()),
                ('custparent_id', models.BigIntegerField()),
                ('customer_id', models.BigIntegerField()),
                ('product_num', models.BigIntegerField()),
                ('productid', models.CharField(blank=True, db_column='ProductID', max_length=60, null=True)),
                ('gtin', models.CharField(blank=True, db_column='GTIN', max_length=14, null=True)),
                ('contract_number', models.CharField(blank=True, max_length=24, null=True)),
                ('internalitemnumber', models.CharField(blank=True, db_column='InternalItemNumber', max_length=120, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, db_column='Price', decimal_places=6, max_digits=12, null=True)),
                ('priceunitid', models.CharField(blank=True, db_column='PriceUnitID', max_length=12, null=True)),
                ('lastedit', models.DateTimeField(blank=True, db_column='LastEdit', null=True)),
                ('lastedituserid', models.CharField(blank=True, db_column='LastEditUserID', max_length=24, null=True)),
                ('categoryid', models.CharField(blank=True, db_column='CategoryID', max_length=120, null=True)),
                ('code', models.CharField(blank=True, db_column='Code', max_length=20, null=True)),
                ('glcode', models.CharField(blank=True, db_column='GLCode', max_length=50, null=True)),
                ('dispunitid', models.CharField(blank=True, db_column='DispUnitID', max_length=12, null=True)),
                ('dispconversion', models.DecimalField(blank=True, db_column='DispConversion', decimal_places=2, max_digits=12, null=True)),
                ('minimum', models.DecimalField(blank=True, db_column='Minimum', decimal_places=2, max_digits=12, null=True)),
                ('maximum', models.DecimalField(blank=True, db_column='Maximum', decimal_places=2, max_digits=12, null=True)),
                ('qtyonhand', models.DecimalField(blank=True, db_column='QtyOnHand', decimal_places=2, max_digits=12, null=True)),
                ('countuom', models.CharField(blank=True, db_column='CountUOM', max_length=12, null=True)),
                ('autoadded', models.IntegerField(blank=True, db_column='AutoAdded', null=True)),
                ('purchloweruom', models.IntegerField(blank=True, db_column='PurchLowerUOM', null=True)),
                ('deletesync', models.IntegerField(blank=True, db_column='DeleteSync', null=True)),
                ('deletedtm', models.DateTimeField(blank=True, db_column='DeleteDTM', null=True)),
                ('deletereplaceproductid', models.CharField(blank=True, db_column='DeleteReplaceProductID', max_length=120, null=True)),
                ('active', models.IntegerField(blank=True, db_column='Active', null=True)),
            ],
            options={
                'db_table': '`medprocure_portal`.`contract_price`',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Custparent',
            fields=[
                ('custparent_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('comm_queue', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.CharField(blank=True, db_column='EMail', max_length=255, null=True)),
                ('invoice_email', models.CharField(blank=True, db_column='Invoice_EMail', max_length=128, null=True)),
                ('portal_id', models.IntegerField(blank=True, null=True)),
                ('sentupdate', models.DateTimeField(blank=True, db_column='SentUpdate', null=True)),
                ('webaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('webext', models.CharField(blank=True, max_length=3, null=True)),
                ('passcode', models.CharField(blank=True, db_column='PassCode', max_length=128, null=True)),
                ('autoapprove', models.IntegerField(blank=True, db_column='AutoApprove', null=True)),
                ('testaccount', models.IntegerField(blank=True, db_column='TestAccount', null=True)),
                ('privateemail', models.IntegerField(blank=True, db_column='PrivateEmail', null=True)),
                ('forcemanponum', models.IntegerField(blank=True, db_column='ForceManPONum', null=True)),
                ('procuretopay', models.IntegerField(blank=True, db_column='ProcureToPay', null=True)),
                ('medassets_member', models.IntegerField(blank=True, db_column='MedAssets_Member', null=True)),
                ('medassets_facnum', models.IntegerField(blank=True, db_column='MedAssets_FacNum', null=True)),
                ('hideglorder', models.IntegerField(blank=True, db_column='HideGLOrder', null=True)),
                ('searchall', models.IntegerField(blank=True, db_column='SearchAll', null=True)),
                ('accountlabel', models.CharField(blank=True, db_column='AccountLabel', max_length=50, null=True)),
                ('inhouselabel', models.CharField(blank=True, db_column='InHouseLabel', max_length=50, null=True)),
                ('privatelabellogo', models.CharField(blank=True, db_column='PrivateLabelLogo', max_length=120, null=True)),
                ('hin', models.CharField(blank=True, db_column='HIN', max_length=9, null=True)),
                ('gln', models.CharField(blank=True, db_column='GLN', max_length=13, null=True)),
                ('shiptoattn', models.CharField(blank=True, db_column='ShiptoAttn', max_length=64, null=True)),
                ('shiptoaddress', models.CharField(blank=True, db_column='ShiptoAddress', max_length=64, null=True)),
                ('shiptocity', models.CharField(blank=True, db_column='ShiptoCity', max_length=64, null=True)),
                ('shiptostateprov', models.CharField(blank=True, db_column='ShiptoStateProv', max_length=24, null=True)),
                ('shiptopostalcode', models.CharField(blank=True, db_column='ShiptoPostalCode', max_length=24, null=True)),
                ('shiptophone', models.CharField(blank=True, db_column='ShiptoPhone', max_length=24, null=True)),
                ('shiptofax', models.CharField(blank=True, db_column='ShiptoFax', max_length=24, null=True)),
                ('multivendor', models.IntegerField(blank=True, db_column='MultiVendor', null=True)),
                ('lockformulary', models.IntegerField(blank=True, db_column='LockFormulary', null=True)),
                ('active', models.IntegerField(blank=True, db_column='Active', null=True)),
                ('autoadded', models.IntegerField(blank=True, db_column='AutoAdded', null=True)),
                ('allowpatientedit', models.IntegerField(blank=True, db_column='AllowPatientEdit', null=True)),
                ('displaymaxonorders', models.IntegerField(blank=True, db_column='DisplayMaxOnOrders', null=True)),
            ],
            options={
                'db_table': '`medprocure_portal`.`custparent`',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('portal_id', models.BigIntegerField()),
                ('distributor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gln', models.CharField(blank=True, db_column='GLN', max_length=13, null=True)),
                ('short_desc', models.CharField(blank=True, max_length=60, null=True)),
                ('long_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('comm_queue', models.CharField(blank=True, max_length=128, null=True)),
                ('autoacknowledge', models.IntegerField(db_column='AutoAcknowledge')),
                ('webaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('webext', models.CharField(blank=True, max_length=3, null=True)),
                ('passcode', models.CharField(blank=True, db_column='PassCode', max_length=128, null=True)),
                ('pmtattnto', models.CharField(blank=True, db_column='PmtAttnTo', max_length=64, null=True)),
                ('pmtaddress', models.CharField(blank=True, db_column='PmtAddress', max_length=64, null=True)),
                ('pmtcity', models.CharField(blank=True, db_column='PmtCity', max_length=64, null=True)),
                ('pmtstateprov', models.CharField(blank=True, db_column='PmtStateProv', max_length=24, null=True)),
                ('pmtpostalcode', models.CharField(blank=True, db_column='PmtPostalCode', max_length=24, null=True)),
                ('pmtphone', models.CharField(blank=True, db_column='PmtPhone', max_length=24, null=True)),
                ('pmtfax', models.CharField(blank=True, db_column='PmtFax', max_length=24, null=True)),
                ('pmtlogo', models.CharField(blank=True, db_column='PmtLogo', max_length=64, null=True)),
                ('pmttermsconditions', models.TextField(blank=True, db_column='PmtTermsConditions', null=True)),
                ('pmtinvoiceinfo', models.TextField(blank=True, db_column='PmtInvoiceInfo', null=True)),
                ('pmtinvoicelegal', models.TextField(blank=True, db_column='PmtInvoiceLegal', null=True)),
                ('privatelabel', models.IntegerField(blank=True, db_column='PrivateLabel', null=True)),
                ('privatelabellogo', models.CharField(blank=True, db_column='PrivateLabelLogo', max_length=64, null=True)),
                ('privatelabelsalesurl', models.CharField(blank=True, db_column='PrivateLabelSalesURL', max_length=255, null=True)),
                ('privatelabelsupporturl', models.CharField(blank=True, db_column='PrivateLabelSupportURL', max_length=255, null=True)),
                ('privatelabelemailfrom', models.CharField(blank=True, db_column='PrivateLabelEmailFrom', max_length=60, null=True)),
                ('privatelabelemailheader', models.TextField(blank=True, db_column='PrivateLabelEmailHeader', null=True)),
                ('privatelabelemailfooter', models.TextField(blank=True, db_column='PrivateLabelEmailFooter', null=True)),
                ('punchoutenabled', models.IntegerField(blank=True, db_column='PunchoutEnabled', null=True)),
                ('punchouturl', models.CharField(blank=True, db_column='PunchoutURL', max_length=125, null=True)),
                ('punchoutsecret', models.CharField(blank=True, db_column='PunchoutSecret', max_length=75, null=True)),
                ('punchoutmode', models.CharField(blank=True, db_column='PunchoutMode', max_length=50, null=True)),
                ('punchoutcert', models.CharField(blank=True, db_column='PunchoutCert', max_length=50, null=True)),
                ('punchoutcustdomain', models.CharField(blank=True, db_column='PunchoutCustDomain', max_length=50, null=True)),
                ('punchoutdebug', models.IntegerField(blank=True, db_column='PunchoutDebug', null=True)),
                ('punchoutencode', models.IntegerField(blank=True, db_column='PunchoutEncode', null=True)),
                ('punchoutencodeurl', models.IntegerField(blank=True, db_column='PunchoutEncodeURL', null=True)),
                ('backfill', models.IntegerField(db_column='Backfill')),
                ('formularyrestricteditall', models.IntegerField(db_column='FormularyRestrictEditAll')),
                ('relayforward', models.IntegerField(db_column='RelayForward')),
                ('privateemail', models.IntegerField(db_column='PrivateEmail')),
                ('usestrictlinenumbers', models.IntegerField(db_column='UseStrictLineNumbers')),
                ('vmi', models.IntegerField(db_column='VMI')),
                ('shiptoaddresschangenotify', models.IntegerField(db_column='ShipToAddressChangeNotify')),
                ('allowlinenotes', models.IntegerField(db_column='AllowLineNotes')),
                ('returnacknowledgment', models.IntegerField(db_column='ReturnAcknowledgment')),
                ('acknowledgefromformulary', models.IntegerField(db_column='AcknowledgeFromFormulary')),
                ('isa_link', models.CharField(blank=True, db_column='ISA_Link', max_length=15, null=True)),
            ],
            options={
                'db_table': '`medprocure_portal`.`distributor`',
                'managed': False,
            },
        ),
    ]
