# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class IdProduct(models.Model):
    product_num = models.BigAutoField(primary_key=True)
    productid = models.CharField(db_column='ProductID', unique=True, max_length=60)  # Field name made lowercase.
    business_id = models.BigIntegerField()
    distributor_id = models.BigIntegerField()
    manufacturer_id = models.BigIntegerField()
    manufacturerpartnumber = models.CharField(db_column='ManufacturerPartNumber', max_length=120)  # Field name made lowercase.
    primaryvendoritemnumber = models.CharField(db_column='PrimaryVendorItemNumber', max_length=120)  # Field name made lowercase.
    internalitemnumber = models.CharField(db_column='InternalItemNumber', max_length=120)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    manufactured = models.PositiveIntegerField(db_column='Manufactured')  # Field name made lowercase.
    kit = models.PositiveIntegerField(db_column='Kit')  # Field name made lowercase.
    active = models.PositiveIntegerField(db_column='Active')  # Field name made lowercase.
    perpetual = models.PositiveIntegerField(db_column='Perpetual')  # Field name made lowercase.
    service = models.IntegerField(db_column='Service')  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=25)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=25)  # Field name made lowercase.
    gtin = models.CharField(db_column='GTIN', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'id_product'


class IdProductUnitConv(models.Model):
    unitid = models.CharField(db_column='UnitID', max_length=60)  # Field name made lowercase.
    convqty = models.DecimalField(db_column='ConvQty', max_digits=20, decimal_places=8)  # Field name made lowercase.
    convunitid = models.CharField(db_column='ConvUnitID', max_length=12)  # Field name made lowercase.
    productid = models.ForeignKey(IdProduct, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'id_product_unit_conv'
