from django.contrib import admin
from covidregister.register.models import (
    Patient,
    Drug,
    PreexistingMedication,
    CovidMedication,
    Disease,
    PreexistingIllness,
    CovidIllness,
)

admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Disease)
admin.site.register(PreexistingMedication)
admin.site.register(PreexistingIllness)
admin.site.register(CovidIllness)
admin.site.register(CovidMedication)
