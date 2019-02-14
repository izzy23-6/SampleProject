from django.db import models
from ..models import IdProduct


class ProductUnitConvManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('productid')

    # def product_conv_factor(self, productid, unitid, convunitid, convqty):
    #     self.productid = productid
    #     self.unitid = fromunit
    #     self.convunitid = tounit
    #     self.convqty = convqty


class IdProductUnitConv(models.Model):
    productid = models.ForeignKey(IdProduct, db_column='ProductID', related_name='puc', to_field='productid', max_length=60, on_delete=models.CASCADE)
    unitid = models.CharField(db_column='UnitID', max_length=60)
    convqty = models.DecimalField(db_column='ConvQty', max_digits=20, decimal_places=8)
    convunitid = models.CharField(db_column='ConvUnitID', max_length=12)

    class Meta:
        db_table = 'id_product_unit_conv'

    # @property
    # def conv(self):
    #     return 
