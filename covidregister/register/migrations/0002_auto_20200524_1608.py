# Generated by Django 3.0.6 on 2020-05-24 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medication',
            name='drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Drug'),
        ),
        migrations.AddField(
            model_name='medication',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Patient'),
        ),
        migrations.AddField(
            model_name='illness',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.Disease'),
        ),
        migrations.AddField(
            model_name='illness',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Patient'),
        ),
    ]
