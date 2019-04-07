from xmlrpc.client import DateTime

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView

from calendarOfDiseases.form import MeasurementForm
from database.models import Measurement, Indicator
from database.models import Patient
from django.db.models import Count, DateTimeField
from django.shortcuts import render, redirect
from django.views import View

dis = 1


class DiseaseView(View):
    def get(self, request, disease):
        MeasurementView.setDis(disease)
        return render(
            request,
            'disease.html',
            {
                'user_profile': request.user,
                'form': MeasurementForm()
            }
        )


class MeasurementView(View):
    disa = 1

    def setDis(self, dis):
        self.disa = dis

    def get(self, request, date):
        measurement = Measurement.objects.filter(date=date, patient__user=request.user, type__diseases__in=self.disa)
        return render(
            request,
            'measurement.html',
            {
                'user_profile': request.user,
                'measurement': measurement,
                'form': MeasurementForm()
            }
        )
