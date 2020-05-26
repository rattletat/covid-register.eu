from django import forms
from django.forms import inlineformset_factory
from dal import autocomplete

from .models import (
    Patient,
    PreexistingIllness,
    CovidIllness,
    PreexistingMedication,
    CovidMedication,
    CovidTherapy,
    Disease,
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Fieldset,
    Div,
    Row,
    HTML,
    Submit,
)
from .custom_layout_object import Formset
import re


class PreexistingIllnessForm(forms.ModelForm):
    class Meta:
        model = PreexistingIllness
        fields = ("disease", "start", "severity")
        widgets = {
            "disease": autocomplete.ModelSelect2(
                url="register:disease-autocomplete",
                attrs={"data-placeholder": "Search ICD system"},
            ),
            "start": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Row(
                    Field("disease", wrapper_class="col-md-6"),
                    Field("start", wrapper_class="col-md-3"),
                    Field("severity", wrapper_class="col-md-3"),
                    Field("DELETE", wrapper_class="col-md-2"),
                ),
                css_class="formset_div-{}".format(self.formtag_prefix),
            )
        )


class CovidIllnessForm(forms.ModelForm):
    COVID_CODES = ["U07.1", "U07.2"]
    disease = forms.ModelChoiceField(
        queryset=Disease.objects.filter(code__in=COVID_CODES)
    )

    class Meta:
        model = CovidIllness
        fields = (
            "disease",
            "start",
            "end",
            "days_symptom_free",
            "days_mild",
            "days_moderate",
            "days_severe",
        )
        widgets = {
            "start": forms.widgets.DateInput(attrs={"type": "date"}),
            "end": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Row(
                    Field("disease", wrapper_class="col-md-6"),
                    Field("start", wrapper_class="col-md-3"),
                    Field("end", wrapper_class="col-md-3"),
                ),
                Row(
                    Field("days_symptom_free", wrapper_class="col-md-3"),
                    Field("days_mild", wrapper_class="col-md-3"),
                    Field("days_moderate", wrapper_class="col-md-3"),
                    Field("days_severe", wrapper_class="col-md-3"),
                ),
            )
        )


class MedicationForm(forms.ModelForm):
    class Meta:
        fields = (
            "drug",
            "start",
            "end",
            "dosage",
            "dosage_form",
            "dosage_unit",
            "count",
            "time_unit",
        )
        widgets = {
            "start": forms.widgets.DateInput(attrs={"type": "date"}),
            "end": forms.widgets.DateInput(attrs={"type": "date"}),
            "drug": autocomplete.ModelSelect2(
                url="register:drug-autocomplete",
                attrs={"data-placeholder": "Search ATC system"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))


class PreexistingMedicationForm(MedicationForm):
    exclude = ["end"]

    class Meta(MedicationForm.Meta):
        model = PreexistingMedication

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Div(
                Row(
                    Field("drug", wrapper_class="col-md-6"),
                    Field("start", wrapper_class="col-md-6"),
                ),
                Row(
                    Field("dosage", wrapper_class="col-md-2"),
                    Field("dosage_unit", wrapper_class="col-md-3"),
                    Field("count", wrapper_class="col-md-2"),
                    Field("time_unit", wrapper_class="col-md-2"),
                    Field("dosage_form", wrapper_class="col-md-3"),
                    Field("DELETE"),
                ),
                css_class="formset_div-{}".format(self.formtag_prefix),
            ),
        )


class CovidMedicationForm(MedicationForm):
    class Meta(MedicationForm.Meta):
        model = CovidMedication

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Div(
                Row(
                    Field("drug", wrapper_class="col-md-6"),
                    Field("start", wrapper_class="col-md-3"),
                    Field("end", wrapper_class="col-md-3"),
                ),
                Row(
                    Field("dosage", wrapper_class="col-md-2"),
                    Field("dosage_unit", wrapper_class="col-md-3"),
                    Field("count", wrapper_class="col-md-2"),
                    Field("time_unit", wrapper_class="col-md-2"),
                    Field("dosage_form", wrapper_class="col-md-3"),
                    Field("DELETE"),
                ),
                css_class="formset_div-{}".format(self.formtag_prefix),
            ),
        )


class CovidTherapyForm(forms.ModelForm):
    class Meta:
        model = CovidTherapy
        fields = ("therapy_form", "start", "end")
        widgets = {
            "start": forms.widgets.DateInput(attrs={"type": "date"}),
            "end": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Row(
                    Field("therapy_form", wrapper_class="col-md-6"),
                    Field("start", wrapper_class="col-md-3"),
                    Field("end", wrapper_class="col-md-3"),
                    Field("DELETE"),
                ),
                css_class="formset_div-{}".format(formtag_prefix),
            ),
        )


PreIllnessFormSet = inlineformset_factory(
    Patient,
    PreexistingIllness,
    form=PreexistingIllnessForm,
    can_delete=True,
    extra=1,
)
PreexistingMedicationFormSet = inlineformset_factory(
    Patient,
    PreexistingMedication,
    form=PreexistingMedicationForm,
    can_delete=True,
    extra=1,
)
CovidIllnessFormSet = inlineformset_factory(
    Patient,
    CovidIllness,
    form=CovidIllnessForm,
    can_delete=False,
    extra=1,
    min_num=1,
    max_num=1,
)
CovidMedicationFormSet = inlineformset_factory(
    Patient, CovidMedication, form=CovidMedicationForm, can_delete=True, extra=1,
)
CovidTherapyFormSet = inlineformset_factory(
    Patient, CovidTherapy, form=CovidTherapyForm, can_delete=True, extra=1
)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["identifer", "birth_year", "sex", "status"]

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-vertical"
        self.helper.css_class = "input-group"
        self.helper.layout = Layout(
            Div(
                Div(
                    Field("identifer", wrapper_class="col-md-4",),
                    Field("birth_year", wrapper_class="col-md-3"),
                    Field("sex", wrapper_class="col-md-2"),
                    Field("status", wrapper_class="col-md-3"),
                    css_class="form-row",
                ),
                Fieldset("Pre-Existing Medication", Formset("medication")),
                Fieldset("Pre-Existing Diseases", Formset("illnesses")),
                Fieldset("COVID-19", Formset("covid")),
                Fieldset(
                    "Medication during COVID infection", Formset("covid_medication")
                ),
                Fieldset("Therapy during COVID infection", Formset("covid_therapy")),
                HTML("<br>"),
                Div(
                    HTML(
                        '<a class="btn btn-danger col-md-6" href={% url "register:list" %}>Cancel</a>'
                    ),
                    Submit("Save", "Save", css_class="btn-primary col-md-6"),
                    css_class="form-row",
                ),
            )
        )
