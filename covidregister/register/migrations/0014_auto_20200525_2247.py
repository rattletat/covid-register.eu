# Generated by Django 3.0.6 on 2020-05-25 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20200525_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)], verbose_name='Year of birth'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Female'), (2, 'Male'), (3, 'Other')], null=True),
        ),
    ]