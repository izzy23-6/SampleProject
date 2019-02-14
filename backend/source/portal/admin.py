from django.contrib import admin
from .models import *

# Register your models here.

class CustparentAdmin(admin.ModelAdmin):
    list_display = (
        'custparent_id',
        'name',
        'comm_queue',
        'email',
        'invoice_email',
        'portal_id',
        'sentupdate',
        'webaddress',
        'webext',
        'passcode',
        'autoapprove',
        'testaccount',
        'privateemail',
        'forcemanponum',
        'procuretopay',
        'medassets_member',
        'medassets_facnum',
        'hideglorder',
        'searchall',
        'accountlabel',
        'inhouselabel',
        'privatelabellogo',
        'hin',
        'gln',
        'shiptoattn',
        'shiptoaddress',
        'shiptocity',
        'shiptostateprov',
        'shiptopostalcode',
        'shiptophone',
        'shiptofax',
        'multivendor',
        'lockformulary',
        'active',
        'autoadded',
        'allowpatientedit',
        'displaymaxonorders',
    )
    ordering = ['custparent_id']
    search_fields = ['custparent_id']

class ContractPriceAdmin(admin.ModelAdmin):
    list_display = (
        'contractprice_id',
        'portal_id',
        'distributor_id',
        'custparent_id',
        'customer_id',
        'product_num',
        'productid',
        'gtin',
        'contract_number',
        'internalitemnumber',
        'description',
        'price',
        'priceunitid',
        'lastedit',
        'lastedituserid',
        'categoryid',
        'code',
        'glcode',
        'dispunitid',
        'dispconversion',
        'minimum',
        'maximum',
        'qtyonhand',
        'countuom',
        'autoadded',
        'purchloweruom',
        'deletesync',
        'deletedtm',
        'deletereplaceproductid',
        'active',
    )

class DistributorAdmin(admin.ModelAdmin):
    list_display = (
        'portal_id',
        'distributor_id',
        'gln',
        'short_desc',
        'long_desc',
        'comm_queue',
        'autoacknowledge',
        'webaddress',
        'webext',
        'passcode',
        'pmtattnto',
        'pmtaddress',
        'pmtcity',
        'pmtstateprov',
        'pmtpostalcode',
        'pmtphone',
        'pmtfax',
        'pmtlogo',
        'pmttermsconditions',
        'pmtinvoiceinfo',
        'pmtinvoicelegal',
        'privatelabel',
        'privatelabellogo',
        'privatelabelsalesurl',
        'privatelabelsupporturl',
        'privatelabelemailfrom',
        'privatelabelemailheader',
        'privatelabelemailfooter',
        'punchoutenabled',
        'punchouturl',
        'punchoutsecret',
        'punchoutmode',
        'punchoutcert',
        'punchoutcustdomain',
        'punchoutdebug',
        'punchoutencode',
        'punchoutencodeurl',
        'backfill',
        'formularyrestricteditall',
        'relayforward',
        'privateemail',
        'usestrictlinenumbers',
        'vmi',
        'shiptoaddresschangenotify',
        'allowlinenotes',
        'returnacknowledgment',
        'acknowledgefromformulary',
        'isa_link',
    )

class IdProductAdmin(admin.ModelAdmin):
    list_display = (
        'portal_id',
        'distributor_id',
        'product_num',
        'productid',
        'manufacturerpartnumber',
        'manufacturernamecode',
        'gtin',
        'alternatepartnumber',
        'description',
        'active',
        'purchloweruom',
        'cost',
        'costunitid',
        'lastedit',
        'mpn_match',
    )


admin.site.register(Custparent, CustparentAdmin)
admin.site.register(ContractPrice, ContractPriceAdmin)
# admin.site.register(Distributor, DistributorAdmin)
# admin.site.register(IdProduct, IdProductAdmin)