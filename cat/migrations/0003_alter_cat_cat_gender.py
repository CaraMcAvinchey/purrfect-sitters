# Generated by Django 3.2 on 2023-05-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0002_auto_20230512_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10),
        ),
    ]
