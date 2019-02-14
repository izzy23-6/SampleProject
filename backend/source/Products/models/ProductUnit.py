from django.db import models
from .Products import *


class IdProductUnit(models.Model):
        productid = models.ForeignKey('Products.IdProduct', to_field='productid', related_name='product_unit', db_column='ProductID', on_delete=models.CASCADE)
        unitid = models.CharField(db_column='UnitID', max_length=60)  # Field name made lowercase.
        typeid = models.CharField(db_column='TypeID', max_length=16)  # Field name made lowercase.

        class Meta:
            db_table = 'id_product_unit'
            # unique_together = (('productid', 'unitid', 'typeid'),)
