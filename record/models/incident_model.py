from django.db import models


class Incident(models.Model):
    """
    Model used for incidents that have occurred.
    """

    nhs_reg_number = models.CharField(max_length=20, blank=False, verbose_name='NHS Registration Number')
    """The NHS registration number of the patient."""

    address = models.CharField(max_length=50, blank=False, verbose_name='Address')
    """The address of the patient."""

    post_code = models.CharField(max_length=10, blank=False, verbose_name='Post Code')
    """The post code of the patient."""

    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    """The description of the incident."""

    time_occurred = models.DateTimeField(blank=True, null=True, verbose_name='Time Occurred')
    """The time that the incident occurred."""

    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Longitude')
    """The longitude that the incident occurred at."""

    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Latitude')
    """The latitude that the incident occurred at."""

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
