# Generated by Django 5.0.6 on 2024-06-16 15:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=128)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='america_car_renting.state')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(db_index=True, max_length=128)),
                ('vehicle_model', models.CharField(max_length=128)),
                ('vehicle_make', models.CharField(max_length=128)),
                ('vehicle_type', models.CharField(max_length=128)),
                ('vehicle_year', models.CharField(max_length=128)),
                ('renter_trips_taken', models.IntegerField()),
                ('review_count', models.IntegerField()),
                ('rate_daily', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(5000)])),
                ('ranking', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('fuel_type', models.CharField(max_length=128)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='america_car_renting.city')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_renting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownner_id', models.CharField(db_index=True, max_length=128)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='america_car_renting.vehicle')),
            ],
        ),
    ]