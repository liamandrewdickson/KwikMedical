from django.urls import path

from record.views import overview, incident_form, rescue_request_form, incident_list, medical_record_list, \
    edit_medical_record_form

app_name = "record"

urlpatterns = [
    path('', overview, name='overview'),
    path('incident/', incident_form, name='incident_form'),
    path('list/incident/', incident_list, name='incident_list'),
    path('list/medical_record/', medical_record_list, name='medical_record_list'),
    path('rescue_request/<int:incident_id>', rescue_request_form, name='rescue_request_form'),
    path('medical_record/<int:medical_record_id>', edit_medical_record_form, name='edit_medical_record_form'),
]
