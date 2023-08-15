from django.urls import path

from record.views import overview

app_name = "record"

urlpatterns = [
    path('', overview, name='overview'),
]