from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from database.models import Doctor, Patient


def addPatient(request):
    if request.method == "POST":
        patient = request.POST.get("patient")
        doctor = Doctor.objects.get(user=request.user)
        patient = Patient.objects.get(id=patient)
        patient.doctors.add(doctor)
        return render(request, 'Doctor/patient_info.html', {
            "patient": request.POST.get("patient")
        })
    else:
        patient_full_name = str(request.GET.get("s"))
        pfn = patient_full_name.split(' ')
        patients = Patient.objects.filter((Q(user__first_name=pfn[0]) | Q(user__last_name=pfn[0]))
                                          & (Q(user__first_name=pfn[1]) | Q(
            user__last_name=pfn[0])))
        return render(request, 'Doctor/patient_info.html', {
            'patients': patients
        })


def getPatientInfo(request):
    if request.method == "GET":
        doctor = Doctor.objects.filter(user=request.user)
        patient = request.GET.get("patient")
        patients = Patient.objects.filter(doctors__in=doctor)
    return render(request, 'Doctor/patient_info.html', {
        'patients': patients,
        'patient': patient,
        'doctor': doctor,
    })
