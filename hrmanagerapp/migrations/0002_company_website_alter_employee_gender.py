# Generated by Django 4.2.3 on 2023-08-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmanagerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100),
        ),
    ]