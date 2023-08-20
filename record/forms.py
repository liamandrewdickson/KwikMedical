from django.forms import ModelForm, Textarea, DateTimeField


class PatientForm(ModelForm):
    """
    Form for the Patient table.
    """

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        from record.models import Patient
        model = Patient
        fields = '__all__'


class IncidentForm(ModelForm):
    """
    Form for the Incident table.
    """
    from tempus_dominus.widgets import DateTimePicker

    time_occurred = DateTimeField(
        widget=DateTimePicker(
            attrs={
                'input_toggle': True,
                'icon_toggle': False,
                'autocomplete': 'off',
            }
        ),
        label='Date Occurred',
        required=True,
    )

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        from record.models import Incident
        model = Incident
        fields = '__all__'

        widgets = {
            'description': Textarea(attrs={'rows': 2}),
            'action_taken': Textarea(attrs={'rows': 2}),
        }


class RescueRequestForm(ModelForm):
    """
    Form for the RescueRequest table.
    """

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        from record.models import RescueRequest
        model = RescueRequest
        fields = '__all__'

        widgets = {
            'description': Textarea(attrs={'rows': 2}),
        }


class MedicalRecordForm(ModelForm):
    """
    Form for the MedicalRecord table.
    """

    class Meta:
        """
        Model Meta is for “anything that’s not a field”, such as ordering options (ordering),
        database table name (db_table), or human-readable singular and plural names.
        """
        from record.models import MedicalRecord
        model = MedicalRecord
        fields = '__all__'

        widgets = {
            'description': Textarea(attrs={'rows': 2}),
            'treatment': Textarea(attrs={'rows': 2}),
        }
