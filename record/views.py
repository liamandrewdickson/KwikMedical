from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


@login_required()
def overview(request):
    """
    Generates and renders the overview screen,
    :param request: The Web Server Gateway Interface request.
    :return: A rendered view of overview screen.
    """

    args = {}
    return render(request, 'record/overview.html', args)


@login_required()
def incident_form(request):
    """
    Generates and renders the Incident form.
    :param request: The Web Server Gateway Interface request.
    :return: A rendered Incident form
    """
    from django.http import HttpResponseRedirect
    from record.forms import IncidentForm, PatientForm
    from record.models import Patient, MedicalRecord

    if request.method == 'POST':
        args = {'incident_form': IncidentForm(request.POST), 'patient_form': PatientForm(request.POST)}
        print(args['incident_form'].errors)

        if args['incident_form'].is_valid() and args['patient_form'].is_valid():
            incident = args['incident_form'].save()

            # Checks if a Patient already exists in the Patient table.
            is_there_a_patient = Patient.objects.filter(nhs_reg_number__exact=incident.nhs_reg_number)

            # If a Patient does not exist, it will create one.
            if not is_there_a_patient:
                args['patient_form'].save()

            patient = get_object_or_404(Patient, nhs_reg_number__icontains=incident.nhs_reg_number)
            medical_record = MedicalRecord(patient=patient, incident=incident)
            medical_record.save()

            return HttpResponseRedirect('/rescue_request/' + str(incident.pk))
    else:
        args = {'incident_form': IncidentForm(), 'patient_form': PatientForm()}

    return render(request, 'record/forms/incident_form.html', args)


@login_required()
def rescue_request_form(request, incident_id: int):
    """
    Generates and renders the Rescue Request form.
    :param incident_id: ID of the Incident.
    :param request: The Web Server Gateway Interface request.
    :return: A rendered Incident form
    """
    from django.http import HttpResponseRedirect
    from record.forms import RescueRequestForm
    from record.models import MedicalRecord, Incident, Patient, Hospital
    from scipy.spatial import KDTree

    if request.method == 'POST':
        redirect = request.POST['redirect']
        args = {'rescue_request_form': RescueRequestForm(request.POST)}
        print(args['rescue_request_form'].errors)
        if args['rescue_request_form'].is_valid():
            args['rescue_request_form'].save()
            return HttpResponseRedirect(redirect)
    else:
        incident = get_object_or_404(Incident, pk=incident_id)

        incident_location = list(incident.location)
        incident_location.reverse()

        hospitals = Hospital.objects.filter(deleted=False).values_list('location', flat=True)
        list_of_hospitals = []

        for hospital in hospitals:
            conv = list(hospital)
            conv.reverse()
            list_of_hospitals.append(conv)

        tree = KDTree(list_of_hospitals)
        closest = tree.query(incident_location)
        list_of_hospitals[closest[1]].reverse()
        closest_converted = tuple(list_of_hospitals[closest[1]])

        closest_hospital = get_object_or_404(Hospital, location=closest_converted)

        patient_exists = Patient.objects.filter(nhs_reg_number__icontains=incident.nhs_reg_number)
        if patient_exists:
            patient = get_object_or_404(Patient, nhs_reg_number__icontains=incident.nhs_reg_number)
            args = {
                'rescue_request_form': RescueRequestForm(initial={'patient': patient, 'hospital': closest_hospital, }),
                'medical_records': MedicalRecord.objects.filter(patient=patient)}

        else:
            args = {'rescue_request_form': RescueRequestForm(initial={'hospital': closest_hospital, }),
                    'medical_records': MedicalRecord.objects.none()}

    return render(request, 'record/forms/rescue_request_form.html', args)


@login_required()
def incident_list(request):
    """
    Generates and renders the incident list.
    :param request: The Web Server Gateway Interface request.
    :return: A rendered list of incidents.
    """
    from record.models import Incident

    args = {'incident_records': Incident.objects.all().order_by('time_occurred')}

    return render(request, 'record/incident_list.html', args)


@login_required()
def medical_record_list(request):
    """
    Generates and renders the medical record list.
    :param request: The Web Server Gateway Interface request.
    :return: A rendered list of incidents.
    """
    from record.models import MedicalRecord

    args = {'medical_records': MedicalRecord.objects.all()}

    return render(request, 'record/medical_record_view.html', args)
