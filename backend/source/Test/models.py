from django.db import models


class EmployeeProfile(models.Model):
    custparent = models.ManyToManyField('portal.Custparent')

    class Meta:
        db_table = 'EmployeeProfile'

# class Relation(models.Model):
#     custparent = models.ForeignKey(Custparent, models.DO_NOTHING)
#     user = models.ForeignKey('User', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'relation'
#         unique_together = (('user', 'custparent'),)
