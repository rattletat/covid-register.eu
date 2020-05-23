from django.contrib import admin
from covidregister.register.models import Patient, Drug, Medication, Disease, Illness

admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Medication)
admin.site.register(Disease)
admin.site.register(Illness)
