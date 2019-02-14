from django.contrib import admin
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_num',
        'productid',
        'manufacturerpartnumber',
        'description',
        'manufactured',
        'kit',
        'active',
        'perpetual',
        'service',
        'primaryvendoritemnumber',
        'size',
        'type',
        'internalitemnumber',
        'gtin',
        'cost',
        'costunitid'
    )


class ProductAliasAdmin(admin.ModelAdmin):
    list_display = (
        'productid',
        'alias',
        'isbarcode',
        'isprintbarcode'
    )


class ProductCostAdmin(admin.ModelAdmin):
    list_display = (
        'productid',
        'cost',
        'costunitid',
        'effectivedate',
        'contract'
    )


class ProductUnitConvAdmin(admin.ModelAdmin):
    list_display = (
        # 'productid',
        'unitid',
        'convqty',
        'convunitid'
    )


admin.site.register(IdProduct, ProductAdmin)
admin.site.register(IdProductUnitConv, ProductUnitConvAdmin)
# admin.site.register(IdProductAlias, ProductAliasAdmin)
# admin.site.register(IdProductCost, ProductCostAdmin)