import datetime
from sqlite3.dbapi2 import Date

from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.utils.timezone import now
from django.views import View
from django.views.generic import ListView

from calendarOfDiseases.form import MeasurementForm
from database.models import Measurement, Indicator
from database.models import Patient
from django.db.models import Count, DateTimeField
from django.shortcuts import render, redirect
from django.views import View

dis = 1


class MeasurementView(View):
    disa = 0

    def setDis(self, dis):
        self.disa = dis

    def get(self, request, date):
        measurements = Measurement.objects.filter(date=date, patient__user=request.user, type__diseases__in=self.disa)
        return render(request, 'measurement.html',
                      {
                          'measurements': measurements,
                          'disease': self.disa,
                      }
                      )


def measurementCreateView(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            type1 = form.cleaned_data['type']
            patient = Patient.objects.filter(user=request.user)[0]
            testimony = form.cleaned_data['testimony']
            comment = form.cleaned_data['comment']
            measurement = Measurement.objects.create(date=now, type=type1, patient=patient, testimony=testimony,
                                                     comment=comment)
            measurement.save()
        else:
            redirect('lk')
    else:
        form = MeasurementForm()
        return render(request, 'create_measurement.html', {'form': form})
