# Generated by Django 2.2.6 on 2020-02-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_merge_20200210_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='stripe_token',
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='stripe_account_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='stripe_bankaccount_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]