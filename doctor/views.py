from django.contrib import auth
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from database.models import Doctor, Patient


def addPatient(request):
    if request.method == "POST":
        oms = request.POST.get("oms")
        try:
            patient = Patient.objects.get(oms=oms)
        except(Patient.DoesNotExist):
            return redirect('/doctor/profile')
        doctor = Doctor.objects.get(user=request.user)
        patient.doctors.add(doctor)
    return redirect('/doctor/profile')


def getPatientInfo(request):
    doctor1 = Doctor.objects.filter(user=request.user)
    patient = request.GET.get("patient")
    patients = Patient.objects.filter(doctors__in=doctor1)
    doctor = Doctor.objects.get(user=request.user)
    return render(request, 'Doctor/patient_info.html', {
        'patients': patients,
        'patient': patient,
        'doctor': doctor,
    })


def deletePatient(request):
    patient = Patient.objects.get(id=request.POST.get("patient"))
    doctor = Doctor.objects.get(user=request.user)
    patient.doctors.remove(doctor)
    patient.save()
    return redirect('/doctor/profile')


def doctorProfile(request):
    doctor = Doctor.objects.get(user=request.user)
    doctor2 = Doctor.objects.filter(user=request.user)
    patients = Patient.objects.filter(doctors__in=doctor2)
    print(request.user.first_name)
    print(doctor)
    print(request.user)
    if request.method == 'POST':
        doctor = Doctor.objects.get(user=request.user)
        first_name = request.POST.get("first_name")
        second_name = request.POST.get("second_name")
        last_name = request.POST.get("last_name")
        license = request.POST.get("license")
        birth_date = request.POST.get("birth_date")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        user = doctor.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        doctor.second_name = second_name
        doctor.date_of_birthday = birth_date
        doctor.gender = gender
        doctor.city = city
        doctor.phone_number = phone_number
        doctor.license = license
        doctor.save()

    return render(request, 'Doctor/preferences.html', {
        'patients': patients,
        'doctor': doctor,
    })


def passchange(request):
    doctor1 = Doctor.objects.filter(user=request.user)
    patients = Patient.objects.filter(doctors__in=doctor1)
    doctor = Doctor.objects.get(user=request.user)
    if request.method == 'POST':
        user = request.user
        username = user.username
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if user.check_password(password):
            if password1 == password2:
                user.set_password(password1)
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return HttpResponseRedirect('/')
    return render(request, 'Doctor/passchange.html', {
        'patients': patients,
        'doctor': doctor,
    })
