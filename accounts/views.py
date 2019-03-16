from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.form import SignUpFormDoctor
from accounts.form import SignUpFormPatient


def signup_doctor(request):
    if request.method == 'POST':
        form = SignUpFormDoctor(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.doctor.username = form.cleaned_data('username')
            user.doctor.password = form.cleaned_data('password1')
            user.doctor.first_name = form.cleaned_data('first_name')
            user.doctor.last_name = form.cleaned_data('last_name')
            user.doctor.date_of_birthday = form.cleaned_data('date_of_birthday')
            user.doctor.gender = form.cleaned_data.get('gender')
            user.doctor.city = form.cleaned_data.get('city')
            user.doctor.phone_number = form.cleaned_data.get('phone_number')
            user.doctor.name_of_organisation = form.cleaned_data('name_of_organisation')
            user.doctor.type = form.cleaned_data.get('type')
            user.doctor.email = form.cleaned_data.get('email')
            user.save()
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
            user = form.save()
            user.refresh_from_db()
            user.patient.username = form.cleaned_data('username')
            user.patient.password = form.cleaned_data('password1')
            user.patient.first_name = form.cleaned_data('first_name')
            user.patient.last_name = form.cleaned_data('last_name')
            user.patient.date_of_birthday = form.cleaned_data('date_of_birthday')
            user.patient.gender = form.cleaned_data.get('gender')
            user.patient.city = form.cleaned_data.get('city')
            user.patient.phone_number = form.cleaned_data.get('phone_number')
            user.patient.email = form.cleaned_data.get('email')
            user.patient.weight = form.cleaned_data.get('weight')
            user.patient.height = form.cleaned_data.get('height')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpFormPatient()
    return render(request, 'signup.html', {'form': form})