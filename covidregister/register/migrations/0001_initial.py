# Generated by Django 3.0.6 on 2020-05-24 16:08

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='ICD-Code')),
                ('name', models.TextField(unique=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='ATC-Code')),
                ('name', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('severity', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('outcome', models.IntegerField(choices=[(1, 'Patient cured'), (2, 'Patient died')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('dosage', models.PositiveIntegerField()),
                ('dosage_unit', models.PositiveIntegerField(choices=[(1, 'milligram'), (2, 'gram')])),
                ('dosage_form', models.PositiveIntegerField(choices=[(1, 'Oral'), (2, 'Ophthalmic'), (3, 'Inhalation'), (4, 'Parenteral'), (5, 'Topical'), (6, 'Suppository')])),
                ('count', models.PositiveIntegerField(verbose_name='Dosage quantity')),
                ('time_unit', models.PositiveIntegerField(choices=[(1, 'day'), (2, 'week')], verbose_name='per')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('identifer', models.CharField(max_length=10, verbose_name='Patient ID')),
                ('birthday', models.DateField(verbose_name='Date of birth')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
