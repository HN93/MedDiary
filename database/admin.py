from django.contrib import admin
from .models import Patient, Doctor, Disease, DoctorType, Indicator, Measurement


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patient._meta.fields]

    class Meta:
        model = Patient


class IndicatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Indicator._meta.fields]

    class Meta:
        model = Indicator


class DoctorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Doctor._meta.fields]

    class Meta:
        model = Doctor


class DiseaseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Disease._meta.fields]

    class Meta:
        model = Disease


class DoctorTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DoctorType._meta.fields]

    class Meta:
        model = DoctorType


class MeasurementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Measurement._meta.fields]

    class Meta:
        model = Measurement


admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(DoctorType, DoctorTypeAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Measurement, MeasurementAdmin)
