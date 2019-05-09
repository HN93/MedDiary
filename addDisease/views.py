from django.shortcuts import render, redirect

from database.models import Patient, Disease


def addDisease(request):
    if request.method == "POST":
        patient = Patient.objects.get(user=request.user)
        disease = request.POST.get("disease")
        disease = Disease.objects.filter(id=disease)
        patient.diseases.add(disease.first())
        patient.save()
    return redirect('/patient')
