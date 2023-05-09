# Generated by Django 3.2 on 2023-05-09 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_age', models.CharField(choices=[('kitten', '3 years and younger'), ('teenager', '4-9 years old'), ('adult', '10-15 years old'), ('geriatric', 'Above 16 years old')], max_length=10)),
                ('cat_gender', models.CharField(choices=[('M', 'Female'), ('F', 'Male')], max_length=2)),
                ('cat_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('cat_description', models.TextField(blank=True, null=True)),
                ('vet_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('profile_updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cat Profiles',
            },
        ),
    ]
