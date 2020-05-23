from django import forms
from django.forms import inlineformset_factory
from dal import autocomplete

from .models import Patient, Illness, Medication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Fieldset,
    Div,
    Row,
    HTML,
    ButtonHolder,
    Submit,
    Column,
    Hidden,
)
from .custom_layout_object import Formset
import re


class IllnessForm(forms.ModelForm):
    class Meta:
        model = Illness
        fields = ("disease", "start", "end", "severity", "outcome")
        widgets = {
            "disease": autocomplete.ModelSelect2(
                url="register:disease-autocomplete",
                attrs={"data-placeholder": "Search ATC system"},
            ),
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
                Field("DELETE", wrapper_class="col-md-2"),
                Row(
                    Field("disease", wrapper_class="col-md-8"),
                    Field("severity", wrapper_class="col-md-4"),
                ),
                Row(
                    Field("start", wrapper_class="col-md-4"),
                    Field("end", wrapper_class="col-md-4"),
                    Field("outcome", wrapper_class="col-md-4"),
                ),
                css_class="formset_div-{}".format(formtag_prefix),
            )
        )


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
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
                attrs={"data-placeholder": "Search ICD system"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub("-[0-9]+$", "", kwargs.get("prefix", ""))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field("DELETE"),
                Row(
                    Field("drug", wrapper_class="col-md-8"),
                    Field("dosage_form", wrapper_class="col-md-4"),
                ),
                Row(
                    Field("start", wrapper_class="col-md-4"),
                    Field("dosage", wrapper_class="col-md-4"),
                    Field("count", wrapper_class="col-md-4"),
                ),
                Row(
                    Field("end", wrapper_class="col-md-4"),
                    Field("dosage_unit", wrapper_class="col-md-4"),
                    Field("time_unit", wrapper_class="col-md-4"),
                ),
                css_class="formset_div-{}".format(formtag_prefix),
            ),
        )


IllnessInlineFormSet = inlineformset_factory(
    Patient, Illness, form=IllnessForm, can_delete=True, extra=1,
)
MedicationInlineFormSet = inlineformset_factory(
    Patient, Medication, form=MedicationForm, can_delete=True, extra=1,
)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["id", "birthday"]
        widgets = {
            "birthday": forms.widgets.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-vertical"
        self.helper.label_class = "col-md-12 create-label"
        self.helper.field_class = "col-md-12"
        self.helper.css_class = "input-group"
        self.helper.layout = Layout(
            Div(
                Div(
                    Field(
                        "id", placeholder="E.g. 12345678", wrapper_class="col-md-6"
                    ),
                    Field("birthday", wrapper_class="col-md-6"),
                    css_class="form-row",
                ),
                Fieldset("Pre-Existing Diseases", Formset("illnesses")),
                HTML("<br>"),
                Fieldset("Medication", Formset("medication")),
                HTML("<br>"),
                Div(
                    HTML(
                        '<a class="btn btn-danger col-md-6" href={% url "register:list" %}>Cancel</a>'
                    ),
                    HTML("<button class='btn-primary col-md-6 '>Save</button>"),
                    css_class="form-row",
                ),
            )
        )
