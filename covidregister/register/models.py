from django.conf import settings
from datetime import datetime
from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from django.core.validators import MinValueValidator, MaxValueValidator
from model_utils.models import TimeStampedModel, StatusModel


class Patient(StatusModel, TimeStampedModel):
    STATUS = Choices(
        ("active", _("Active")),
        ("recovered", _("Recovered")),
        ("death", _("Death")),
    )
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    identifer = models.CharField("Patient ID", max_length=10)
    sex = models.PositiveSmallIntegerField(
        choices=[(1, "Female"), (2, "Male"), (3, "Other")], null=True, blank=True,
    )
    birth_year = models.PositiveSmallIntegerField(
        "Year of birth",
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Patient {self.identifer}"


class Drug(models.Model):
    code = models.CharField("ATC-Code", primary_key=True, max_length=7)
    name = models.TextField("Description")

    def __str__(self):
        return f"{self.code:7} - {self.name}"


class Medication(models.Model):
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

    start = models.DateField("Start of medication", null=True, blank=True)
    end = models.DateField("End of medication", null=True, blank=True)

    dosage = models.PositiveSmallIntegerField(null=True, blank=True)
    dosage_unit = models.PositiveSmallIntegerField(
        choices=MASS, null=True, blank=True
    )
    dosage_form = models.PositiveSmallIntegerField(
        choices=DOSAGE_FORM, null=True, blank=True
    )
    count = models.PositiveSmallIntegerField("Quantity", null=True, blank=True)
    time_unit = models.PositiveSmallIntegerField(
        "per", choices=TIME_UNIT, null=True, blank=True
    )

    class Meta:
        abstract = True


class PreexistingMedication(Medication):
    pass


class CovidMedication(Medication):
    pass


class Disease(models.Model):
    code = models.CharField("ICD-Code", primary_key=True, max_length=7)
    name = models.TextField("Description", unique=True)

    def __str__(self):
        return f"{self.code:7} - {self.name}"


class PreexistingIllness(TimeStampedModel):
    SEVERITY = Choices(
        (1, "symptom_free", _("no symptoms")),
        (2, "mild", _("mild")),
        (3, "moderate", _("moderate")),
        (4, "severe", _("severe")),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, models.PROTECT)

    start = models.DateField("Start of symptoms", null=True, blank=True)
    severity = models.PositiveSmallIntegerField(
        choices=SEVERITY, null=True, blank=True
    )


class CovidIllness(TimeStampedModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, models.PROTECT, null=True, blank=True)

    start = models.DateField("Start of symptoms", null=True, blank=True)
    end = models.DateField("End of symptoms", null=True, blank=True)

    days_symptom_free = models.PositiveSmallIntegerField(
        "Days symptom free", default=0, null=True, blank=True
    )
    days_mild = models.PositiveSmallIntegerField(
        "Days mild", default=0, null=True, blank=True
    )
    days_moderate = models.PositiveSmallIntegerField(
        "Days moderate", default=0, null=True, blank=True
    )
    days_severe = models.PositiveSmallIntegerField(
        "Days severe", default=0, null=True, blank=True
    )


class CovidTherapy(TimeStampedModel):
    THERAPY_FORM = Choices((1, "ventilator", _("Ventilator")))

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    therapy_form = models.PositiveSmallIntegerField(
        choices=THERAPY_FORM, null=True, blank=True
    )
    start = models.DateField("Start of therapy", null=True, blank=True)
    end = models.DateField("End of therapy", null=True, blank=True)
