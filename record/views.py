from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


@login_required()
def overview(request):
    """
    Generates and renders the overview screen,
    :param request: The Web Server Gateway Interface request.
    :return: A rendered view of overview screen.
    """

    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    # mapbox_access_token = 'pk.my_mapbox_access_token'
    #
    # args = {'mapbox_access_token': mapbox_access_token}
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
    from record.forms import IncidentForm

    if request.method == 'POST':
        form = request.POST.get('form')
        redirect = request.POST['redirect']
        args = {'incident_form': IncidentForm(request.POST)}
        print(args['incident_form'].errors)
        if args['incident_form'].is_valid():
            args['incident_form'].save()
            return HttpResponseRedirect(redirect)
    else:
        args = {'incident_form': IncidentForm()}

    return render(request, 'record/forms/incident_form.html', args)


@login_required()
def rescue_request_form(request, incident_id: int):
    """
    Generates and renders the Rescue Request form.
    :param request: The Web Server Gateway Interface request.
    :return: A rendered Incident form
    """
    from django.http import HttpResponseRedirect
    from record.forms import RescueRequestForm
    from record.models import RescueRequest, Incident, Patient

    if request.method == 'POST':
        form = request.POST.get('form')
        redirect = request.POST['redirect']
        args = {'rescue_request_form': RescueRequestForm(request.POST)}
        print(args['rescue_request_form'].errors)
        if args['rescue_request_form'].is_valid():
            args['rescue_request_form'].save()
            return HttpResponseRedirect(redirect)
    else:
        incident = get_object_or_404(Incident, pk=incident_id)

        patient = get_object_or_404(Patient, nhs_reg_number__icontains=incident.nhs_reg_number)

        args = {'rescue_request_form': RescueRequestForm(initial={'patient': patient, })}

    return render(request, 'record/forms/rescue_request_form.html', args)

