# Generated by Django 2.2.8 on 2021-09-11 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0112_auto_20210824_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='employersubscription',
            name='stripe_sub',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
