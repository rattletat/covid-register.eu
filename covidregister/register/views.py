from dal import autocomplete
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PatientForm, IllnessInlineFormSet, MedicationInlineFormSet
from .models import Patient, Disease, Drug


class PatientListView(LoginRequiredMixin, ListView):

    template_name = "list.html"
    model = Patient
    paginate_by = 4

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
            data["illnesses"] = IllnessInlineFormSet(self.request.POST)
            data["medication"] = MedicationInlineFormSet(self.request.POST)
        else:
            data["illnesses"] = IllnessInlineFormSet()
            data["medication"] = MedicationInlineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        illnesses = context["illnesses"]
        medication = context["medication"]
        with transaction.atomic():
            form.instance.doctor = self.request.user
            self.object = form.save()
            if illnesses.is_valid():
                illnesses.instance = self.object
                illnesses.save()
            if medication.is_valid():
                medication.instance = self.object
                medication.save()
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
            data["illnesses"] = IllnessInlineFormSet(self.request.POST, instance=obj)
            data["medication"] = MedicationInlineFormSet(self.request.POST, instance=obj)
        else:
            data["illnesses"] = IllnessInlineFormSet(instance=obj)
            data["medication"] = MedicationInlineFormSet(instance=obj)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        illnesses = context["illnesses"]
        medication = context["medication"]
        with transaction.atomic():
            form.instance.doctor = self.request.user
            self.object = form.save()
            if illnesses.is_valid():
                illnesses.instance = self.object
                illnesses.save()
            if medication.is_valid():
                medication.instance = self.object
                medication.save()
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
            qs = qs.filter(code__istartswith=self.q).union(qs.filter(name__contains=self.q))

        return qs


class DrugAutocomplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Drug.objects.all()

        if self.q:
            qs = qs.filter(code__istartswith=self.q).union(qs.filter(name__contains=self.q))

        return qs
