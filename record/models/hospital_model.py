from django.db import models


class Hospital(models.Model):
    """
    Model used for the regional hospitals.
    """

    from mapbox_location_field.models import LocationField

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name')
    """The name of the hospital."""

    location = LocationField(null=True, blank=True,
                             map_attrs={"center": [-3.2141745, 55.933486], "marker_color": "blue"},
                             default=[-3.2141745, 55.933486])
    """The location of the hospital."""

    deleted = models.BooleanField(default=False, null=False, verbose_name='Deleted')
    """Is this hospital entry deleted?"""

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        db_table = 'Hospital'

    def __str__(self):
        return str(self.name)
