from django.db import models
from django.db.models import F, Q
from django.shortcuts import *
from source.CDR import SpanningForeignKey
from Patients.models import *
from Products.models import *
from users.models import *
from source.PriceConv import *
from decimal import *


class RelateionshipManager(models.Manager):
    """  This class runs a custom quert that runs a left join whenever the ChargesSupply model is called """
    def get_queryset(self):
        queryset = super().get_queryset().select_related('trans', 'contractprice')
        return queryset

""" ChargesSupply Table Controller """
class ChargesSupply(models.Model):
    trans = models.ForeignKey('Charges', db_column='TransID', on_delete=models.CASCADE)
    LineNum = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    LocationID = models.IntegerField(blank=True, null=True)
    LastEdited = models.DateTimeField(auto_now=True)
    ProductNum = models.BigIntegerField()
    productid = models.CharField(db_column='ProductID', max_length=60, blank=True, null=True)
    BillingMethod = models.CharField(max_length=60, blank=True, null=True)
    Description = models.CharField(max_length=255)
    Quantity = models.DecimalField(max_digits=12, decimal_places=2)
    UnitID = models.CharField(max_length=12)
    contractprice = SpanningForeignKey('portal.ContractPrice', db_column='contractprice', related_name='products', on_delete=models.CASCADE)

    objects = models.Manager()
    rel = RelateionshipManager()

    class Meta:
        db_table = 'id_hcm_charges_supply'
        unique_together = ("trans", "LineNum")

    def __str__(self):
        return f'{str(self.trans)}'
    
    def t(y, z):
        """ This function takes in fields and returns the values if they are not null """
        return z if z is not None else 0
    
    @property
    def priceunitid(self):
        """ Returns convunitid from ContractPrice table """
        productid = self.productid
        t = self.t
        c = ChargesSupply.objects.select_related('contractprice__productid').filter(contractprice__productid=productid).values_list(F('contractprice__dispunitid'), flat=True)
        cu = [t(x) for x in c]
        # cu = t(c)
        return cu[0]
    
    @property
    def costunitid(self):
        """ Returns convunitid from ContractPrice table """
        productid = self.productid
        t = self.t
        c = ChargesSupply.rel.filter(contractprice__productid=productid).select_related('contractprice__productid').values_list(F('contractprice__priceunitid'), flat=True)
        cu = [t(x) for x in c]
        # cu = t(c)
        return cu[0]

    @property
    def cost(self):
        """ Returns convqty from ContractPrice """
        productid = self.productid
        t = self.t
        c = ChargesSupply.rel.filter(contractprice__productid=productid).select_related().values_list(F('contractprice__price'), flat=True)
        cq = [t(x) for x in c]
        return cq[0]

    @property
    def convqty(self):
        """ Returns convqty from ContractPrice """
        productid = self.productid
        t = self.t
        c = ChargesSupply.objects.distinct().filter(productid=productid).select_related('contractprice').values_list(F('contractprice__dispconversion'), flat=True)
        cq = [t(x) for x in c]
        return cq[0]

    @property
    def quantity(self):
        """ Returns Quantity """
        return self.Quantity

    def get_product_unit_conversion(self):
        """ Calculates the price of the product based on their units """
        FromQty = self.quantity
        conv_factor = self.convqty
        ToQty = FromQty * conv_factor
        return ToQty


    def get_price(self):
        """ Calculates the price based on the, Quantity and the product_unit_conversion() """
        Quantity = self.get_product_unit_conversion()
        priceamount = 100.0 
        cost = self.cost
        if "MU".lower() is not None:
            price = Decimal(cost) * (1 + (Decimal(priceamount) / 100))
        amount = price * Quantity
        return amount

    @property
    def unitprice(self):
        """ Calculates the total price for the products """
        priceamount = 100.0
        cost = self.cost
        Quantity = self.get_product_unit_conversion()
        if "MU".lower() is not None:
            price = Decimal(cost) * (1 + (Decimal(priceamount) / 100))
        amount = self.get_price() / self.quantity
        return "${:,.2f}".format(amount)
    
    @property
    def p(self):
        """ This function displays the product in a better format """
        price = self.get_price()
        return "${:,.2f}".format(price)


    def save(self, *args, **kwargs):
        """ Increments the LineNum column in the database whenever there the date, Trans, and or patient data has changed. """
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
