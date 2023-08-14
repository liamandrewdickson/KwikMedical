from django.db import models


class Hospital(models.Model):
    """
    Model used for the regional hospitals.
    """

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name')
    """The name of the hospital."""

    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Longitude')
    """The longitude that the hospital."""

    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Latitude')
    """The latitude that the hospital."""

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
