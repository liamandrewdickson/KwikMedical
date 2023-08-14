from django.db import models


class Patient(models.Model):
    """
    Model used for the patients of the NHS.
    """

    nhs_reg_number = models.CharField(max_length=20, blank=False, verbose_name='NHS Registration Number')
    """The NHS registration number of the patient."""

    full_name = models.CharField(max_length=100, blank=False, verbose_name='Full Name')
    """The fullname of the patient."""

    phone_number = models.CharField(max_length=20, null=False, blank=True, verbose_name='Phone Number')
    """The patient's phone number."""

    address = models.CharField(max_length=50, blank=False, verbose_name='Address')
    """The address of the patient."""

    post_code = models.CharField(max_length=10, blank=False, verbose_name='Post Code')
    """The post code of the patient."""

    deleted = models.BooleanField(default=False, null=False, verbose_name='Deleted')
    """Is this patient entry deleted?"""

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        db_table = 'Patient'

    def __str__(self):
        return str(self.nhs_reg_number)
