# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ContractPrice(models.Model):
    contractprice_id = models.BigAutoField(primary_key=True)
    portal_id = models.BigIntegerField()
    distributor_id = models.BigIntegerField()
    custparent_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    product_num = models.BigIntegerField()
    productid = models.CharField(db_column='ProductID', max_length=60, blank=True, null=True)  # Field name made lowercase.
    gtin = models.CharField(db_column='GTIN', max_length=14, blank=True, null=True)  # Field name made lowercase.
    contract_number = models.CharField(max_length=24, blank=True, null=True)
    internalitemnumber = models.CharField(db_column='InternalItemNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    priceunitid = models.CharField(db_column='PriceUnitID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lastedit = models.DateTimeField(db_column='LastEdit', blank=True, null=True)  # Field name made lowercase.
    lastedituserid = models.CharField(db_column='LastEditUserID', max_length=24, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.CharField(db_column='CategoryID', max_length=120, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    glcode = models.CharField(db_column='GLCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dispunitid = models.CharField(db_column='DispUnitID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dispconversion = models.DecimalField(db_column='DispConversion', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    minimum = models.DecimalField(db_column='Minimum', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    maximum = models.DecimalField(db_column='Maximum', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtyonhand = models.DecimalField(db_column='QtyOnHand', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    countuom = models.CharField(db_column='CountUOM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    autoadded = models.IntegerField(db_column='AutoAdded', blank=True, null=True)  # Field name made lowercase.
    purchloweruom = models.IntegerField(db_column='PurchLowerUOM', blank=True, null=True)  # Field name made lowercase.
    deletesync = models.IntegerField(db_column='DeleteSync', blank=True, null=True)  # Field name made lowercase.
    deletedtm = models.DateTimeField(db_column='DeleteDTM', blank=True, null=True)  # Field name made lowercase.
    deletereplaceproductid = models.CharField(db_column='DeleteReplaceProductID', max_length=120, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contract_price'
