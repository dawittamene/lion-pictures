# Generated by Django 4.1.6 on 2023-10-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0007_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Booking_Date',
            new_name='for_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='date_booking',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]