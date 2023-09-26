# Generated by Django 4.2.5 on 2023-09-26 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(0)]),
        ),
    ]
