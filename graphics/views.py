from django.shortcuts import render
from database.models import Measurement
from database.models import Disease


def getGraph(request):
    if request.method == 'GET':
        disease = request.GET.get("disease")
        measurements = Measurement.objects.filter(patient__user=request.user,
                                                  indicator__diseases__in=Disease.objects.filter(id=disease))
        measurements = measurements.order_by()

    return render(request, 'Patient/graph.html', {
        'measurements': measurements,
        'patient': request.user.patient,
        'diseases': Disease.objects.filter(patient__user=request.user),
        'all_diseases': Disease.objects.exclude(patient__user=request.user),

    })
