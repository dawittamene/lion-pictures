# Generated by Django 4.2.6 on 2023-11-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0016_booking_date_created_contact_date_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
