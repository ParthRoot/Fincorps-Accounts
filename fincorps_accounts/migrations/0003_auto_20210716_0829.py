# Generated by Django 3.2.4 on 2021-07-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fincorps_accounts', '0002_general_ledger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_ledger',
            name='credit',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='general_ledger',
            name='debit',
            field=models.FloatField(default=None),
        ),
    ]
