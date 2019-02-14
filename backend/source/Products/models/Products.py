from django.db import models
from django.db.models import F, Q
# from .ProductConv import *

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('puc').all()


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
    cost = models.DecimalField(db_column='Cost', blank=True, null=True, max_digits=5, decimal_places=2)
    costunitid = models.CharField(db_column='CostUnitID', blank=True, null=True, max_length=5)

    objects = models.Manager()
    pre_select = ProductManager()

    class Meta:
        db_table = 'id_product'

    @property
    def searchProducts(self):
        return f'{self.productid} - {self.description}'

    # @property
    # def puc(self):
    #     return self.idproductunitconv_set.all()

    @property
    def conv(self):
        p = IdProduct.objects
        # pc= IdProdu
        # productid = self.productid
        # convqty = self.puc.filter(productid=productid)
        return p.values_list('puc__convqty', flat=True)[0]
        # return convqty

    def get_product_unit_conv_factor(self, productid, fromunit, tounit):
        pass
