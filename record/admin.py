from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from record.models import Patient, Incident, Hospital, MedicalRecord, RescueRequest

# Used to add the Patient Model to the Django Admin Screen.
admin.site.register(Patient)

# Used to add the Incident Model to the Django Admin Screen.
admin.site.register(Incident, MapAdmin)

# Used to add the Hospital Model to the Django Admin Screen.
admin.site.register(Hospital)

# Used to add the MedicalRecord Model to the Django Admin Screen.
admin.site.register(MedicalRecord)

# Used to add the RescueRequest Model to the Django Admin Screen.
admin.site.register(RescueRequest)
