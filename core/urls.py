from django.urls import path
from .views import (
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingDetailView,
    MappingsByPatientView
)

urlpatterns = [
    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),
    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),
    path('mappings/', MappingListCreateView.as_view()),
    path('mappings/<int:patient_id>/', MappingsByPatientView.as_view(), name='mappings-by-patient'),
    path('mappings/detail/<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),

]