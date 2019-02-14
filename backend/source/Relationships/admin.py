from django.contrib import admin
from .models import *

# Register your models here.


class CustparentAdmin(admin.ModelAdmin):
    list_display = (
        'custparent',
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
    )


# @admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = (
        'distributor',
        'portal_id',
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

# @admin.register(ContractPrice)


class ContractPriceAdmin(admin.ModelAdmin):
    list_display = (
        'contractprice',
        'portal_id',
        'distributor',
        'custparent',
        'customer_id',
        'Product_Num',
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
    search_fields = ('id',)
    # ordering = ('name',)
    filter_horizontal = ()

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'custparent')


admin.site.register(Custparent, CustparentAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(ContractPrice, ContractPriceAdmin)
# admin.site.register(Employee, EmployeeAdmin)
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# class ProfileAdmin(admin.ModelAdmin):
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','custparent')
