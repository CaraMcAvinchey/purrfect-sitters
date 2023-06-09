# Generated by Django 3.2 on 2023-05-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_age',
            field=models.CharField(choices=[('3 years and younger', '3 years and younger'), ('4-9 years old', '4-9 years old'), ('10-15 years old', '10-15 years old'), ('Above 16 years old', 'Above 16 years old')], max_length=50),
        ),
        migrations.AlterField(
            model_name='cat',
            name='cat_gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=2),
        ),
    ]
