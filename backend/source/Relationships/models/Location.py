# from django.conf import settings
# from django.db import models

# from .Custparent import *
# from Charges.models import *
# from users.models import *

# class Location(models.Model):
#     # employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # custparent = models.ForeignKey(Custparent, on_delete=models.CASCADE)
#     custparent = models.ManyToManyField(Custparent, through='Charges.Charges', through_fields=('custparent', 'user'))
#     # custparent_name = models.ForeignKey(Custparent, to_field='name',unique=True)

#     class Meta:
#         db_table = 'Location'
