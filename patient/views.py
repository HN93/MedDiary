from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from database.models import Patient, Disease


def getPatientProfile(request):
    patient = Patient.objects.get(user=request.user)
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        second_name = request.POST.get("second_name")
        last_name = request.POST.get("last_name")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        birth_date = request.POST.get("birth_date")
        oms = request.POST.get("oms")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        city = request.POST.get("city")
        user = patient.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        patient.second_name = second_name
        patient.weight = weight
        patient.height = height
        patient.date_of_birthday = birth_date
        patient.oms = oms
        patient.gender = gender
        patient.city = city
        patient.phone_number = phone_number
        patient.save()
        print(patient)
        print(user)

    return render(request, 'Patient/preferences.html', {
        'patient': patient,
        'diseases': Disease.objects.filter(patient__user=request.user),
        'all_diseases': Disease.objects.exclude
        (patient__user=request.user),

    })


def passchange(request):
    patient = Patient.objects.get(user=request.user)
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
    return render(request, 'Patient/passchange.html', {
        'patient': patient,
        'diseases': Disease.objects.filter(patient__user=request.user),
        'all_diseases': Disease.objects.exclude
        (patient__user=request.user),
    })
