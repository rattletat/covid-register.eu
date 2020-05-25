# Generated by Django 3.0.6 on 2020-05-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20200525_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidtherapy',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='End of therapy'),
        ),
        migrations.AddField(
            model_name='covidtherapy',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='Start of therapy'),
        ),
        migrations.AlterField(
            model_name='covidillness',
            name='days_mild',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Days mild'),
        ),
        migrations.AlterField(
            model_name='covidillness',
            name='days_moderate',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Days moderate'),
        ),
        migrations.AlterField(
            model_name='covidillness',
            name='days_severe',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Days severe'),
        ),
        migrations.AlterField(
            model_name='covidillness',
            name='days_symptom_free',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Days symptom free'),
        ),
        migrations.AlterField(
            model_name='covidmedication',
            name='count',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='covidmedication',
            name='dosage_form',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Oral'), (2, 'Ophthalmic'), (3, 'Inhalation'), (4, 'Parenteral'), (5, 'Topical'), (6, 'Suppository')], null=True),
        ),
        migrations.AlterField(
            model_name='covidmedication',
            name='dosage_unit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'milligram'), (2, 'gram')], null=True),
        ),
        migrations.AlterField(
            model_name='covidmedication',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='Start of medication'),
        ),
        migrations.AlterField(
            model_name='covidmedication',
            name='time_unit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'day'), (2, 'week')], null=True, verbose_name='per'),
        ),
        migrations.AlterField(
            model_name='covidtherapy',
            name='therapy_form',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Ventilator')], null=True),
        ),
        migrations.AlterField(
            model_name='preexistingillness',
            name='severity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'no symptoms'), (2, 'mild'), (3, 'moderate'), (4, 'severe')], null=True),
        ),
        migrations.AlterField(
            model_name='preexistingillness',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='Start of symptoms'),
        ),
        migrations.AlterField(
            model_name='preexistingmedication',
            name='count',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='preexistingmedication',
            name='dosage_form',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Oral'), (2, 'Ophthalmic'), (3, 'Inhalation'), (4, 'Parenteral'), (5, 'Topical'), (6, 'Suppository')], null=True),
        ),
        migrations.AlterField(
            model_name='preexistingmedication',
            name='dosage_unit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'milligram'), (2, 'gram')], null=True),
        ),
        migrations.AlterField(
            model_name='preexistingmedication',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='Start of medication'),
        ),
        migrations.AlterField(
            model_name='preexistingmedication',
            name='time_unit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'day'), (2, 'week')], null=True, verbose_name='per'),
        ),
    ]
