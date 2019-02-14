from django.conf import settings
from django.db import models


from .Custparent import *
from .Distributor import *


class ContractPrice(models.Model):
    contractprice = models.BigAutoField(primary_key=True)
    portal_id = models.BigIntegerField()
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    custparent = models.ForeignKey(Custparent, on_delete=models.CASCADE)
    customer_id = models.BigIntegerField()
    Product_Num = models.BigIntegerField()
    productid = models.CharField(db_column='ProductID', max_length=60, blank=True, null=True)
    gtin = models.CharField(db_column='GTIN', max_length=14, blank=True, null=True)
    contract_number = models.CharField(max_length=24, blank=True, null=True)
    internalitemnumber = models.CharField(db_column='InternalItemNumber', max_length=120, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=6, blank=True, null=True)
    priceunitid = models.CharField(db_column='PriceUnitID', max_length=12, blank=True, null=True)
    lastedit = models.DateTimeField(db_column='LastEdit', blank=True, null=True)
    lastedituserid = models.CharField(db_column='LastEditUserID', max_length=24, blank=True, null=True)
    categoryid = models.CharField(db_column='CategoryID', max_length=120, blank=True, null=True)
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)
    glcode = models.CharField(db_column='GLCode', max_length=50, blank=True, null=True)
    dispunitid = models.CharField(db_column='DispUnitID', max_length=12, blank=True, null=True)
    dispconversion = models.DecimalField(db_column='DispConversion', max_digits=12, decimal_places=2, blank=True,                                  null=True)
    minimum = models.DecimalField(db_column='Minimum', max_digits=12, decimal_places=2, blank=True, null=True)
    maximum = models.DecimalField(db_column='Maximum', max_digits=12, decimal_places=2, blank=True, null=True)
    qtyonhand = models.DecimalField(db_column='QtyOnHand', max_digits=12, decimal_places=2, blank=True,                                                               null=True)
    countuom = models.CharField(db_column='CountUOM', max_length=12, blank=True, null=True)
    autoadded = models.IntegerField(db_column='AutoAdded', blank=True, null=True)
    purchloweruom = models.IntegerField(db_column='PurchLowerUOM', blank=True, null=True)
    deletesync = models.IntegerField(db_column='DeleteSync', blank=True, null=True)
    deletedtm = models.DateTimeField(db_column='DeleteDTM', blank=True, null=True)
    deletereplaceproductid = models.CharField(db_column='DeleteReplaceProductID', max_length=120, blank=True, null=True)
    active = models.IntegerField(db_column='Active', blank=True, null=True)


    class Meta:
        db_table = 'ContractPrice'
        # unique_together= ("Product_Num", "productid")

    # def __str__(self):
    #     return self.contractprice && self.price
    
    @property
    def searchProducts(self):
        return f'{self.productid} - {self.description}'
