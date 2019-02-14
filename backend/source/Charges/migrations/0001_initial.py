# Generated by Django 2.1.5 on 2019-01-22 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import source.CDR


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Patients', '0001_initial'),
        ('portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('TransID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TransDate', models.DateField()),
                ('LastEditDateTime', models.DateTimeField(auto_now=True)),
                ('FromRecurTransID', models.PositiveIntegerField(blank=True, null=True)),
                ('Exported', models.IntegerField(blank=True, null=True)),
                ('custparent', source.CDR.SpanningForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='portal.Custparent')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.IdPatient')),
            ],
            options={
                'db_table': 'id_hcm_charges',
            },
        ),
        migrations.CreateModel(
            name='ChargesSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LineNum', models.PositiveIntegerField(default=1)),
                ('LocationID', models.IntegerField(blank=True, null=True)),
                ('LastEdited', models.DateTimeField(auto_now=True)),
                ('ProductNum', models.BigIntegerField()),
                ('productid', models.CharField(blank=True, db_column='ProductID', max_length=60, null=True)),
                ('BillingMethod', models.CharField(blank=True, max_length=60, null=True)),
                ('Description', models.CharField(max_length=255)),
                ('Quantity', models.DecimalField(decimal_places=4, max_digits=12)),
                ('UnitID', models.CharField(max_length=12)),
                ('contractprice', source.CDR.SpanningForeignKey(db_column='contractprice', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='portal.ContractPrice')),
                ('trans', models.ForeignKey(db_column='TransID', on_delete=django.db.models.deletion.CASCADE, to='Charges.Charges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'id_hcm_charges_supply',
            },
        ),
        migrations.AlterUniqueTogether(
            name='chargessupply',
            unique_together={('trans', 'LineNum')},
        ),
    ]