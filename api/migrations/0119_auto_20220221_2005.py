# Generated by Django 2.2.8 on 2022-02-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0118_auto_20211124_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.URLField(blank=True, default=True, null=True),
        ),
    ]
