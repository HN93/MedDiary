from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.form import SignUpFormDoctor
from django.contrib.auth.forms import AuthenticationForm
from accounts.form import SignUpFormPatient
from database.models import Doctor, Patient, DoctorType
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        try:
            user.save()
        except Exception:
            return render(request, 'sign_up.html')
        user = authenticate(username=user.username, password=password)
        login(request, user)
        if (request.POST.get("ifDoctor") is not None):
            return redirect('signup_doctor')
        else:
            return redirect('signup_patient')
    return render(request, 'sign_up.html')


def signup_doctor(request):
    doctor_types = DoctorType.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        license = request.POST.get('license')
        second_name = request.POST.get('second_name')
        date_of_birthday = request.POST.get('birthday_date')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        name_of_organisation = request.POST.get('organisation')
        doctor_type = request.POST.get('type')
        doctor_type = DoctorType.objects.get(id=doctor_type)
        doctor = Doctor.objects.create(date_of_birthday=date_of_birthday, gender=gender, city=city,
                                       phone_number=phone_number, name_of_organisation=name_of_organisation,
                                       type=doctor_type, user=user, second_name=second_name, license=license)
        try:
            doctor.save()
        except Exception:
            return render(request, 'Doctor/signup.html', {
                'doctor_types': doctor_types,
            })

        login(request, user)
        return redirect('../doctor/profile')
    return render(request, 'Doctor/signup.html', {
        'doctor_types': doctor_types,
    })


def signup_patient(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        date_of_birthday = request.POST.get('date_of_birthday')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        oms = request.POST.get('oms')
        patient = Patient.objects.create(date_of_birthday=date_of_birthday, gender=gender, city=city,
                                         phone_number=phone_number, user=user, weight=weight, height=height, oms=oms)
        try:
            patient.save()
        except Exception:
            return render(request, 'Patient/signup.html')
        return redirect('/patient/profile')
    return render(request, 'Patient/signup.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', )
        password = request.POST.get('password', )
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if Patient.objects.filter(user=user).count() > 0:
                return HttpResponseRedirect('/patient/profile')
            else:
                return HttpResponseRedirect('/doctor/profile')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')
