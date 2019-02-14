from django.conf import settings
from django.db import models

from .Custparent import *
from Charges.models import *
from users.models import *

class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    custparent = models.ForeignKey(Custparent, on_delete=models.CASCADE, blank=True, null=True)
    # charge = models.ManyToManyField('Charges.Charges')

    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return f'{self.custparent}'
