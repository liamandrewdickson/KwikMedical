from django.db import models


class Incident(models.Model):
    """
    Model used for incidents that have occurred.
    """

    from mapbox_location_field.models import LocationField

    nhs_reg_number = models.CharField(max_length=20, blank=False, verbose_name='NHS Registration Number')
    """The NHS registration number of the patient."""

    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    """The description of the incident."""

    time_occurred = models.DateTimeField(blank=True, null=True, verbose_name='Time Occurred')
    """The time that the incident occurred."""

    location = LocationField(null=True, blank=True,
                             map_attrs={"center": [-3.2141745, 55.933486], "marker_color": "blue"},
                             default=[-3.2141745, 55.933486])
    """The location of the Incident."""

    action_taken = models.CharField(max_length=50, blank=True, null=True, verbose_name='Action Taken')
    """The action taken for the incident."""

    minutes_on_call = models.IntegerField(null=False, verbose_name='Minutes on Call')
    """The number of minutes the patient was on call."""

    signed_off = models.BooleanField(default=False, null=False, verbose_name='Deleted')
    """Is this incident entry signed off by the hospital?"""

    deleted = models.BooleanField(default=False, null=False, verbose_name='Deleted')
    """Is this incident entry deleted?"""

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        db_table = 'Incident'

    def __str__(self):
        return str(self.description)
