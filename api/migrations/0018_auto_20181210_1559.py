# Generated by Django 2.0 on 2018-12-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20181206_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clockin',
            old_name='latitude',
            new_name='latitude_in',
        ),
        migrations.RenameField(
            model_name='clockin',
            old_name='longitude',
            new_name='latitude_out',
        ),
        migrations.AddField(
            model_name='clockin',
            name='longitude_in',
            field=models.DecimalField(decimal_places=11, default=0, max_digits=14),
        ),
        migrations.AddField(
            model_name='clockin',
            name='longitude_out',
            field=models.DecimalField(decimal_places=11, default=0, max_digits=14),
        ),
    ]