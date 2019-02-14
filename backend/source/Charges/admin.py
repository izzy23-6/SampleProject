from django.contrib import admin
from .models import *

# Register your models here.


class ChargesAdmin(admin.ModelAdmin):
    list_display = (
        'TransID',
        'TransDate',
        'patient',
        # 'user',
        # 'NumericTransDate',
        'LastEditDateTime',
        'custparent',
        # 'LocationID',
        'FromRecurTransID',
        'Exported',
    )


class ChargesSupplyAdmin(admin.ModelAdmin):
    list_display = (
        'trans',
        'LineNum',
        'LocationID',
        'ProductNum',
        'productid',
        'user',
        'Description',
        'BillingMethod',
        'Quantity',
        'UnitID',
        # 'contractprice',
    )

# class ChargeTransactionsAdmin(admin.ModelAdmin):
#     list_display = (
#         'TransID',
#         'LineNum',
#         'patient',
#         'user',
#         'TransDate',
#         'LastEditDateTime',
#         'custparent',
#         'FromRecurTransID',
#         'BillingMethod',
#         'Exported',
#         'ProductNum',
#         'ProductID',
#         'Description',
#         'Quantity',
#         'UnitID',
#         'Price',
#         'contractprice',
#     )

admin.site.register(Charges, ChargesAdmin)
admin.site.register(ChargesSupply, ChargesSupplyAdmin)
# admin.site.register(ChargeTransactions)
