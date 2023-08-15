from django.urls import path

from record.views import overview, incident_form, rescue_request_form

app_name = "record"

urlpatterns = [
    path('', overview, name='overview'),
    path('incident/', incident_form, name='incident_form'),
    path('rescue_request/<int:incident_id>', rescue_request_form, name='rescue_request_form'),
]