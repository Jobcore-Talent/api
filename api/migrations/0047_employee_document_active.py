# Generated by Django 2.2.4 on 2019-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0046_auto_20191108_1807"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="document_active",
            field=models.BooleanField(default=False),
        ),
    ]
