from django.db import models
from django.db.models import F, Q
# from django.conf import settings
from django.shortcuts import *
from source.CDR import SpanningForeignKey

# from Relationships.models import Custparent, ContractPrice
from Patients.models import *
from Products.models import *
from users.models import *
# from portal.models import *


# class Relationships(models.Manager):
#     pass

class Charges(models.Model):
    TransID = models.BigAutoField(primary_key=True)
    TransDate = models.DateField()
    patient = models.ForeignKey(IdPatient, on_delete=models.CASCADE)
    # NumericTransDate        = models.IntegerField(blank=True, null=True)
    LastEditDateTime = models.DateTimeField(auto_now=True)
    custparent = SpanningForeignKey('portal.Custparent', on_delete=models.CASCADE, related_name="facilities")
    FromRecurTransID = models.PositiveIntegerField(blank=True, null=True)
    Exported = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'id_hcm_charges'
        # unique_together = (("user", "TransDate", "patient"),)

    def __str__(self):
        return f'{str(self.TransID)}'

    # @property
    # def cs(self):
    #     return self.chargessupply_set.all()

    # def save(self, *args, **kwargs):

    #     super(ChargesSupply, self).save(*args, **kwargs).save()


class ChargesSupply(models.Model):
    trans = models.ForeignKey('Charges', db_column='TransID', on_delete=models.CASCADE)
    LineNum = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    LocationID = models.IntegerField(blank=True, null=True)
    LastEdited = models.DateTimeField(auto_now=True)
    ProductNum = models.BigIntegerField()
    productid = models.ForeignKey(IdProduct, db_column='ProductID', to_field='productid', related_name='products', on_delete=models.DO_NOTHING)
    BillingMethod = models.CharField(max_length=60, blank=True, null=True)
    Description = models.CharField(max_length=255)
    Quantity = models.DecimalField(max_digits=12, decimal_places=4)
    UnitID = models.CharField(max_length=12)
    Price = models.DecimalField(max_digits=12, decimal_places=6, max_length=60)

    class Meta:
        db_table = 'id_hcm_charges_supply'
        unique_together = ("trans", "LineNum")

    def __str__(self):
        return f'{str(self.trans)}'
    
    def t(y, z):
        return z
    
    # @property
    # def

    @property
    def convqty(self):
        """ Returns the values from id_product_unit_conv table """
        t = self.t
        c = ChargesSupply.objects.values_list('productid__puc__convqty', flat=True)
        cq = [t(x) for x in c]
        return cq



    # def (self):
    #     # productid = self.productid
    #     t = self.t
    #     cs = ChargesSupply.objects.values_list('productid__puc__convqty', flat=True)
    #     ch = [t(x) for x in cs if x is not None]
    #     # chs = list(map(t, ch))
    #     print(ch)

    # @property
    # def conversion(self):
    #     productid = self.productid
    #     # convqty = IdProduct.objects.filter(puc__convqty=convqty)
    #     # p = IdProduct.objects.all().filter(puc__productid=productid)
    #     # p = ChargesSupply.objects.distinct().prefetch_related('productid').filter(productid__puc__productid=productid).values_list(F('productid__puc__convqty'), flat=True)
    #     # p = ChargesSupply.objects.prefetch_related('productid').filter(productid=productid).values(F('productid__puc__convqty'))
    #     convFactor = ChargesSupply.objects.distinct().prefetch_related('productid').filter(productid=productid).values_list(F('productid__puc__convqty'), flat=True)[0]
    #     return convFactor


    # def get_product_unit_convfactor():
    #     pass

    def save(self, *args, **kwargs):
        def cal_key(trans):
            present_keys = ChargesSupply.objects.filter(trans=trans).order_by('-LineNum').values_list('LineNum', flat=True)

            quantity = self.Quantity

            if present_keys and quantity == 1:
                return present_keys[0] + 1
            elif present_keys and quantity >= 1:
                return present_keys[0]
            else:
                return 1
        LineNum = cal_key(self.trans)
        self.LineNum = LineNum
        super(ChargesSupply, self).save(*args, **kwargs)
