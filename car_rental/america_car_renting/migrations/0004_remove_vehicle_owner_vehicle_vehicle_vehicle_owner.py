# Generated by Django 5.0.6 on 2024-06-22 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('america_car_renting', '0003_rename_vehicle_renting_vehicle_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_owner',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='america_car_renting.vehicle_owner'),
        ),
    ]
