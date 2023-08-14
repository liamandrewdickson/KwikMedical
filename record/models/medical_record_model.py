from django.db import models


class MedicalRecord(models.Model):
    """
    Model used for the medical records of patients and the associated incidents.
    """

    from record.models.patient_model import Patient
    from record.models.incident_model import Incident

    description = models.CharField(max_length=50, blank=True, null=True, verbose_name='Description')
    """The description of the medical record."""

    treatment = models.CharField(max_length=50, blank=True, null=True, verbose_name='Treatment')
    """The treatment the patient received."""

    patient = models.ForeignKey(Patient, models.DO_NOTHING, null=False)
    """The ID of the patient."""

    incident = models.ForeignKey(Incident, models.DO_NOTHING, null=True)
    """The ID of the Incident."""

    deleted = models.BooleanField(default=False, null=False, verbose_name='Deleted')
    """Is this incident entry deleted?"""

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        db_table = 'MedicalRecord'
        verbose_name_plural = "Medical Records"

    def __str__(self):
        return str(self.description)
