from django.db import models
from .Products import *


class IdProductCost(models.Model):
    productid = models.ForeignKey('Products.IdProduct', to_field='productid', related_name='product_cost', db_column='ProductID', on_delete=models.CASCADE)  # Field name made lowercase.
    Cost = models.DecimalField(db_column='Cost', max_digits=12, decimal_places=4)  # Field name made lowercase.
    CostUnitID = models.CharField(db_column='CostUnitID', max_length=12)  # Field name made lowercase.
    EffectiveDate = models.DateField(db_column='EffectiveDate')  # Field name made lowercase.
    Contract = models.CharField(db_column='Contract', max_length=250)  # Field name made lowercase.
    # products = models.ForeignKey('Products.Idproduct', on_delete=models.CASCADE)

    class Meta:
        db_table = 'id_product_cost'
        # unique_together = (('productid', 'EffectiveDate'),)
        
    # def __str__(self):
    #     return self.cost
