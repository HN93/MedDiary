from django.forms import ModelForm

from database.models import Measurement


class MeasurementForm(ModelForm):
    class Meta:
        model = Measurement
        fields = ['measurement']
        labels = {'measurements': ""}