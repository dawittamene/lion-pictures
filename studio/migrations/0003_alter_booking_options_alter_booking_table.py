# Generated by Django 4.1.6 on 2023-10-24 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0002_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='booking',
            table='Booking_table',
        ),
    ]
