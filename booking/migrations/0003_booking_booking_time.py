# Generated by Django 3.2 on 2023-05-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(null=True),
        ),
    ]
