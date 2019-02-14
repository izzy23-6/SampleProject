from django.db import models

class IdProductAlias(models.Model):
    productid = models.ForeignKey('Products.IdProduct', db_column='ProductID', on_delete=models.CASCADE)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=120)  # Field name made lowercase.
    isbarcode = models.PositiveIntegerField(db_column='IsBarCode')  # Field name made lowercase.
    isprintbarcode = models.PositiveIntegerField(db_column='IsPrintBarCode')  # Field name made lowercase.

    class Meta:
        db_table = 'id_product_alias'
        unique_together = (('productid', 'alias'), ('productid', 'isprintbarcode', 'alias'),)

    # def __str__(self):
    #     return f'{self.productid} {self.alias}'
