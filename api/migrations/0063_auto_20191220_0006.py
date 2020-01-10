# Generated by Django 2.2.4 on 2019-12-20 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_merge_20191218_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='total_invites',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='jobcoreinvite',
            name='employer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Employer'),
        ),
        migrations.AddField(
            model_name='position',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DELETED', 'Deleted')], default='ACTIVE', max_length=9),
        ),
        migrations.AddField(
            model_name='profile',
            name='employer_role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('SUPERVISOR', 'Supervisor')], default='ADMIN', max_length=25),
        ),
        migrations.AddField(
            model_name='shiftinvite',
            name='responded_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('DELETED', 'Deleted')], default='ACTIVE', max_length=9),
        ),
    ]
