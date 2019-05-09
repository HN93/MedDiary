import datetime

from django.shortcuts import render
from database.models import Measurement, Indicator, Patient, DoctorType, Doctor
from database.models import Disease


def getGraph(request):
    if request.method == 'GET':
        disease = request.GET.get("disease")
        disease = Disease.objects.filter(id=disease)
        measurements = Measurement.objects.filter(patient__user=request.user,
                                                  indicator__diseases__in=disease).order_by('date', 'indicator__type')
        indicators = Indicator.objects.filter(diseases__in=disease).order_by('type')
        array = []
        j = 0
        row = 0;
        while (j < len(measurements)):
            arr = [str(measurements[j].date)]
            for i in range(len(indicators)):
                try:
                    arr.append(measurements[i + row * len(indicators)].testimony)
                except(IndexError):
                    arr.append(i + (row - 1) * len(indicators))
                j += 1
            array.append(arr)
            row += 1
        print(array)
    return render(request, 'Patient/graph.html', {
        'indicators': indicators,
        'measurements': measurements,
        'patient': request.user.patient,
        'diseases': Disease.objects.filter(patient__user=request.user),
        'all_diseases': Disease.objects.exclude
        (patient__user=request.user),
        'array': array,

    })


def get_graph_doctor(request):
    if request.method == 'GET':
        patient = Patient.objects.get(id=request.GET.get("patient"))
        doctor = Doctor.objects.filter(user=request.user)
        doctor_type = DoctorType.objects.filter(doctor__in=doctor)
        disease = Disease.objects.filter(patient=patient, indicator__diseases__doctorType__in=doctor_type).distinct()
        measurements = Measurement.objects.filter(patient=patient,
                                                  indicator__diseases__in=disease).order_by('date',
                                                                                            'indicator__type').distinct()
        indicators = Indicator.objects.filter(diseases__in=disease).order_by('type').distinct()
        array = []
        j = 0
        row = 0;
        while (j < len(measurements)):
            arr = [str(measurements[j].date)]
            for i in range(len(indicators)):
                try:
                    arr.append(measurements[i + row * len(indicators)].testimony)
                except(IndexError):
                    arr.append(i + (row - 1) * len(indicators))
                j += 1
            array.append(arr)
            row += 1
        print(array)
    return render(request, 'Doctor/graph.html', {
        'indicators': indicators,
        'measurements': measurements,
        'doctor': request.user.doctor,
        'patients': Patient.objects.filter(doctors__in=doctor),
        'array': array,

    })
