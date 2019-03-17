from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.form import SignUpFormDoctor
from django.contrib.auth.forms import AuthenticationForm
from accounts.form import SignUpFormPatient
from database.models import Doctor, Patient
from django.contrib import auth


def signup_doctor(request):
    if request.method == 'POST':
        form = SignUpFormDoctor(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mail = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=mail)
            user = User.objects.get(username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            date_of_birthday = form.cleaned_data['date_of_birthday']
            gender = form.cleaned_data['gender']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            name_of_organisation = form.cleaned_data['name_of_organisation']
            doctor_type = form.cleaned_data['type']
            doctor = Doctor.objects.create(date_of_birthday=date_of_birthday, gender=gender, city=city,
                                           phone_number=phone_number, name_of_organisation=name_of_organisation,
                                           type=doctor_type, user=user)
            doctor.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpFormDoctor()
    return render(request, 'signup.html', {'form': form})


def signup_patient(request):
    if request.method == 'POST':
        form = SignUpFormPatient(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mail = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=mail)
            user = User.objects.get(username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            date_of_birthday = form.cleaned_data['date_of_birthday']
            gender = form.cleaned_data['gender']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            patient = Patient.objects.create(date_of_birthday=date_of_birthday, gender=gender, city=city,
                                             phone_number=phone_number, user=user, weight=weight, height=height)
            patient.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpFormPatient()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', )
        password = request.POST.get('password', )
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        return render(request, 'login.html', {'form': AuthenticationForm})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
