# Generated by Django 3.2.12 on 2022-03-18 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0122_userprofile_stripe_sub_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]