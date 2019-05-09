# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from database.models import Measurement, Indicator, Disease, Doctor
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
        if not Measurement.objects.filter(date=date, indicator=indicator, patient=patient).exists():
            measurement = Measurement.objects.create(indicator=indicator, patient=patient, testimony=testimony,
                                                     comment=comment, date=date)
            measurement.save()

        else:
            measurement = Measurement.objects.filter(date=date, indicator=indicator, patient=patient).last()
            measurement.testimony = testimony
            measurement.comment = comment
            measurement.save()
    return render(request, 'Patient/measurement.html', {
        'indicators': indicators,
        'diseases': Disease.objects.filter(patient__user=request.user),
        'patient': Patient.objects.get(user=request.user),
        'all_diseases': Disease.objects.exclude(patient__user=request.user), })


def addDoctorComment(request):
    patient = request.GET.get('patient')
    doctor = Doctor.objects.filter(id=request.user.id)
    patients = Patient.objects.filter(doctors__in=doctor)

    if request.method == "POST":
        comment = request.POST.get("comment")
        date = request.POST.get("date")
        measurement = Measurement.objects.get(date=date, patient=patient, indicator__diseases__doctorType__in=doctor)
        measurement.doctor_comment = comment
        measurement.save()
    return redirect('/doctor')
