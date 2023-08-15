from django.urls import path

from record.views import overview, incident_form

app_name = "record"

urlpatterns = [
    path('', overview, name='overview'),
    path('incident/', incident_form, name='incident_form'),
]