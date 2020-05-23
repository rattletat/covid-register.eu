# Generated by Django 3.0.6 on 2020-05-23 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
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
                ('dosage', models.PositiveIntegerField(choices=[(1, 'milligram'), (2, 'gram')])),
                ('dosage_form', models.PositiveIntegerField(choices=[(1, 'Oral'), (2, 'Ophthalmic'), (3, 'Inhalation'), (4, 'Parenteral'), (5, 'Topical'), (6, 'Suppository')])),
                ('count', models.PositiveIntegerField()),
                ('time_unit', models.PositiveIntegerField(choices=[(1, 'day'), (2, 'week')])),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Drug')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Patient')),
            ],
            options={
                'abstract': False,
            },
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
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Disease')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
