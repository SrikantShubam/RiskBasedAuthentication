# Generated by Django 4.1 on 2023-05-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0009_alter_data_collected_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_collected',
            name='geolocation_totaltime',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='data_collected',
            name='latitude',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='data_collected',
            name='longitude',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
