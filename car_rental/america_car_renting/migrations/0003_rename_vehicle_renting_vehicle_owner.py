# Generated by Django 5.0.6 on 2024-06-22 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('america_car_renting', '0002_rename_ownner_id_vehicle_renting_owner_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vehicle_renting',
            new_name='Vehicle_owner',
        ),
    ]
