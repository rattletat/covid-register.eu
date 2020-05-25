# Generated by Django 3.0.6 on 2020-05-25 20:21

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='institution',
            field=models.CharField(blank=True, max_length=255, verbose_name='Institution of User'),
        ),
    ]