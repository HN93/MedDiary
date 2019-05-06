# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from database.models import Measurement, Indicator, Disease, MeasurementFrequency
from database.models import Patient


def measurementCreateView(request):
    disease = request.GET.get("disease")
    indicators = Indicator.objects.filter(diseases__in=Disease.objects.filter(id=disease))
    if request.method == 'POST':
        date = request.POST.get("date")
        indicator = request.POST.get("type")
        indicator = Indicator.objects.all().get(id=indicator)
        testimony = request.POST.get("testimony")
        comment = request.POST.get("comment")
        patient = Patient.objects.get(user=request.user)
        mf = MeasurementFrequency.objects.get(patient=patient, indicator=indicator)
        if (Measurement.objects.filter(date=date, indicator=indicator, patient=patient).count() < mf.frequency):
            measurement = Measurement.objects.create(indicator=indicator, patient=patient, testimony=testimony,
                                                     comment=comment, date=date)
            measurement.save()

        else:
            measurement = Measurement.objects.filter(date=date, indicator=indicator, patient=patient).last()
            measurement.indicator = indicator
            measurement.save()
    return render(request, 'Patient/measurement.html', {
        'indicators': indicators,
        'diseases': Disease.objects.filter(patient__user=request.user),
        'patient': Patient.objects.get(user=request.user),
        'all_diseases': Disease.objects.exclude(patient__user=request.user), })
