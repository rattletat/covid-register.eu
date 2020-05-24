from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.models import TimeStampedModel, TimeFramedModel


class Patient(TimeStampedModel):
    identifer = models.CharField("Patient ID", max_length=10)
    birthday = models.DateField("Date of birth")
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)


class Drug(models.Model):
    code = models.CharField("ATC-Code", primary_key=True, max_length=7)
    name = models.TextField("Description")

    def __str__(self):
        return f"{self.code:7} - {self.name}"


class Medication(TimeFramedModel):
    DOSAGE_FORM = Choices(
        (1, "oral", _("Oral")),
        (2, "ophthalmic", _("Ophthalmic")),
        (3, "inhalation", _("Inhalation")),
        (4, "parenteral", _("Parenteral")),
        (5, "topical", _("Topical")),
        (6, "suppository", _("Suppository")),
    )
    TIME_UNIT = Choices((1, "d", _("day")), (2, "w", _("week")),)
    MASS = Choices((1, "mg", _("milligram")), (2, "g", _("gram")),)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.PROTECT)
    dosage = models.PositiveIntegerField()
    dosage_unit = models.PositiveIntegerField(choices=MASS)
    dosage_form = models.PositiveIntegerField(choices=DOSAGE_FORM)
    count = models.PositiveIntegerField("Dosage quantity")
    time_unit = models.PositiveIntegerField("per", choices=TIME_UNIT)


class Disease(models.Model):
    code = models.CharField("ICD-Code", primary_key=True, max_length=7)
    name = models.TextField("Description", unique=True)

    def __str__(self):
        return f"{self.code:7} - {self.name}"


class Illness(TimeStampedModel, TimeFramedModel):
    SEVERITY = [(i, i) for i in range(11)]
    OUTCOME = Choices(
        (1, "cured", _("Patient cured")), (2, "died", _("Patient died")),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, models.PROTECT)
    severity = models.IntegerField(choices=SEVERITY)
    outcome = models.IntegerField(choices=OUTCOME)
