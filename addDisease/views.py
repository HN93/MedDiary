from django.shortcuts import render, redirect

from database.models import Patient, Disease, Indicator, MeasurementFrequency


def addDisease(request):
    if request.method == "POST":
        patient = Patient.objects.get(user=request.user)
        disease = request.POST.get("disease")
        disease = Disease.objects.filter(id=disease)
        patient.diseases.add(disease.first())
        indicators = Indicator.objects.filter(diseases__in=disease)
        for i in indicators:
            if MeasurementFrequency.objects.filter(patient=patient, indicator=i).exists():
                continue
            else:
                measurement_frequency = MeasurementFrequency.objects.create \
                    (indicator=i, patient=patient, frequency=2)
                measurement_frequency.save()
    patient.save()
    return redirect('/patient')
