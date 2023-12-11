# Generated by Django 5.0 on 2023-12-08 11:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transport', '0003_alter_route_destination_alter_route_pickup_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('plate_number', models.CharField(max_length=10)),
                ('seats', models.PositiveIntegerField(default=20)),
                ('is_available', models.BooleanField(default=True)),
                ('full_capacity', models.BooleanField(default=False)),
                ('seats_remaining', models.PositiveIntegerField(blank=True, null=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.route')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.bus')),
            ],
        ),
    ]
