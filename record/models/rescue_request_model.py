from django.db import models


class RescueRequest(models.Model):
    """
    Model used for the rescue requests.
    """

    from record.models import Patient
    from record.models.hospital_model import Hospital

    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Description')
    """The description of the rescue request."""

    patient = models.ForeignKey(Patient, models.DO_NOTHING, null=False)
    """The ID of the patient."""

    hospital = models.ForeignKey(Hospital, models.DO_NOTHING, null=False)
    """The ID of the hospital."""

    deleted = models.BooleanField(default=False, null=False, verbose_name='Deleted')
    """Is this rescue request entry deleted?"""

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        db_table = 'RescueRequest'
        verbose_name_plural = "Rescue Requests"

    def __str__(self):
        return str(self.description)
