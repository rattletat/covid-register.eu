# Generated by Django 3.0.6 on 2020-05-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='dosage_unit',
            field=models.PositiveIntegerField(choices=[(1, 'milligram'), (2, 'gram')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medication',
            name='dosage',
            field=models.PositiveIntegerField(),
        ),
    ]
