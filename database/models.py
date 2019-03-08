from django.db import models


class DoctorType(models.Model):
    name = models.CharField(max_length=20, null=True, blank=False)


class Doctor(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    type = models.ForeignKey(DoctorType, on_delete=models.CASCADE, null=True)
    age = models.DateField(blank=False)
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Disease(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    doctorType = models.ForeignKey(DoctorType, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'


class Patient(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    age = models.DateField(blank=False)
    diseases = models.ManyToManyField(Disease)
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Analysis(models.Model):
    type = models.CharField(max_length=30)
    diseases = models.ManyToManyField(Disease)
