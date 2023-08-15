from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def overview(request):
    """
    Generates and renders the overview screen,
    :param request: The Web Server Gateway Interface request.
    :return: A rendered view of overview screen.
    """
    args = {}
    return render(request, 'record/overview.html', args)
