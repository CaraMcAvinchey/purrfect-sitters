# Generated by Django 3.2 on 2023-05-22 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0009_alter_booking_booking_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('pending_payment', 'Pending'), ('payment_collected', 'Payment Collected'), ('payment_rejected', 'Payment Rejected')], max_length=50)),
                ('street_address1', models.CharField(max_length=80)),
                ('town_or_city', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('order_number', models.CharField(editable=False, max_length=32, unique=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkout', to='booking.booking')),
            ],
        ),
    ]
