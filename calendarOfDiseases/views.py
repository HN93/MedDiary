# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from database.models import Measurement, Indicator, Disease
from database.models import Patient

dis = 1


def measurementCreateView(request):
    if request.method == 'POST':
        date = request.POST.get("date")
        indicator = request.POST.get("type")
        indicator = Indicator.objects.all().get(id=indicator)
        testimony = request.POST.get("testimony")
        comment = request.POST.get("comment")
        patient = Patient.objects.get(user=request.user)
        measurement = Measurement.objects.create(indicator=indicator, patient=patient, testimony=testimony,
                                                 comment=comment, date=date)
        measurement.save()
    return render(request, 'diseases_info.html', {
        'indicators': Indicator.objects.all()
    })


def getGraph(request):
    if request.method == 'GET':
        measurements = Measurement.objects.filter(patient__user=request.user)

    return render(request, 'graphics.html', {
        'measurements': measurements,
    })
