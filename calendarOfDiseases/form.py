from django import forms
from django.forms import ModelForm

from database.models import Indicator
from database.models import Measurement


class MeasurementForm(ModelForm):
    type = forms.ModelChoiceField(queryset=Indicator.objects.all())
    testimony = forms.IntegerField()
    comment = forms.CharField(max_length=20)

    class Meta:
        model = Measurement
        fields = ('type', 'testimony', 'comment')
