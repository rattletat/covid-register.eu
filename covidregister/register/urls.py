from django.urls import path

from .views import (
    PatientCreateView,
    PatientUpdateView,
    PatientListView,
    PatientDeleteView,
    DiseaseAutocomplete,
    DrugAutocomplete,
)

app_name = "register"
urlpatterns = [
    path("list/", PatientListView.as_view(), name="list"),
    path("create/", PatientCreateView.as_view(), name="create"),
    path("update/<int:pk>", PatientUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", PatientDeleteView.as_view(), name="delete"),
    path(
        "disease-autocomplete",
        DiseaseAutocomplete.as_view(),
        name="disease-autocomplete",
    ),
    path(
        "drug-autocomplete",
        DrugAutocomplete.as_view(),
        name="drug-autocomplete",
    ),
]
