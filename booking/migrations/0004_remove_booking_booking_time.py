# Generated by Django 3.2 on 2023-05-18 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
    ]
