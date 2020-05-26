from dal import autocomplete
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import (
    PatientForm,
    PreIllnessFormSet,
    PreexistingMedicationFormSet,
    CovidIllnessFormSet,
    CovidMedicationFormSet,
    CovidTherapyFormSet,
)
from .models import Patient, Disease, Drug


class PatientListView(LoginRequiredMixin, ListView):

    template_name = "list.html"
    model = Patient
    paginate_by = 10

    def get_queryset(self):
        return Patient.objects.filter(doctor=self.request.user)


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "create.html"
    form_class = PatientForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(PatientCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data["medication"] = PreexistingMedicationFormSet(self.request.POST)
            data["illnesses"] = PreIllnessFormSet(self.request.POST)
            data["covid"] = CovidIllnessFormSet(self.request.POST)
            data["covid_medication"] = CovidMedicationFormSet(self.request.POST)
            data["covid_therapy"] = CovidTherapyFormSet(self.request.POST)
        else:
            data["medication"] = PreexistingMedicationFormSet()
            data["illnesses"] = PreIllnessFormSet()
            data["covid"] = CovidIllnessFormSet()
            data["covid_medication"] = CovidMedicationFormSet()
            data["covid_therapy"] = CovidTherapyFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        illnesses = context["illnesses"]
        medication = context["medication"]
        covid = context["covid"]
        covid_medication = context["covid_medication"]
        covid_therapy = context["covid_therapy"]
        with transaction.atomic():
            self.object = obj = form.save(commit=False)
            obj.doctor = self.request.user
            obj.save()
            if illnesses.is_valid():
                illnesses.patient = obj
                illnesses.save()
            if medication.is_valid():
                medication.patient = obj
                medication.save()
            if covid.is_valid():
                covid.patient = obj
                covid.save()
            if covid_medication.is_valid():
                covid_medication.patient = obj
                covid_medication.save()
            if covid_therapy.is_valid():
                covid_therapy.patient = obj
                covid_therapy.save()
        return super(PatientCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("register:list", kwargs={})


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "create.html"

    def get_context_data(self, **kwargs):
        data = super(PatientUpdateView, self).get_context_data(**kwargs)
        obj = get_object_or_404(Patient, pk=self.object.pk)
        if self.request.POST:
            data["medication"] = PreexistingMedicationFormSet(
                self.request.POST, instance=obj
            )
            data["illnesses"] = PreIllnessFormSet(self.request.POST, instance=obj)
            data["covid"] = CovidIllnessFormSet(self.request.POST, instance=obj)
            data["covid_medication"] = CovidMedicationFormSet(
                self.request.POST, instance=obj
            )
            data["covid_therapy"] = CovidTherapyFormSet(
                self.request.POST, instance=obj
            )
        else:
            data["medication"] = PreexistingMedicationFormSet(instance=obj)
            data["illnesses"] = PreIllnessFormSet(instance=obj)
            data["covid"] = CovidIllnessFormSet(instance=obj)
            data["covid_medication"] = CovidMedicationFormSet(instance=obj)
            data["covid_therapy"] = CovidTherapyFormSet(instance=obj)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        illnesses = context["illnesses"]
        medication = context["medication"]
        covid = context["covid"]
        covid_medication = context["covid_medication"]
        covid_therapy = context["covid_therapy"]
        with transaction.atomic():
            form.instance.doctor = self.request.user
            self.object = form.save()
            if illnesses.is_valid():
                illnesses.save()
            if medication.is_valid():
                medication.save()
            if covid.is_valid():
                covid.save()
            if covid_medication.is_valid():
                covid_medication.save()
            if covid_therapy.is_valid():
                covid_therapy.save()
        return super(PatientUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("register:list", kwargs={})


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "delete.html"
    success_url = reverse_lazy("register:list")


class DiseaseAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Disease.objects.all()

        if self.q:
            qs = qs.filter(code__istartswith=self.q).union(
                qs.filter(name__contains=self.q)
            )

        return qs


class DrugAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Drug.objects.all()

        if self.q:
            qs = qs.filter(code__istartswith=self.q).union(
                qs.filter(name__contains=self.q)
            )

        return qs
