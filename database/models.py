from django.utils import timezone
from django.db import models


class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = models.CharField(max_length=45, null=False, blank=False)
    last_name = models.CharField(max_length=45, null=False, blank=False)
    dateOfBirthday = models.DateField(blank=False)
    gender = models.CharField('gender', choices=GENDER_CHOICES, max_length=1, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    city = models.CharField(max_length=45, default=None)
    mail = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length=30, null=False, blank=False, default=None)
    phone_number = models.IntegerField(null=True)

    class Meta:
        abstract = True


class DoctorType(models.Model):
    name = models.CharField(max_length=20, null=True, blank=False)


class Doctor(User):
    type = models.ForeignKey(DoctorType, on_delete=models.CASCADE, null=True)
    name_of_organisation = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Disease(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    doctorType = models.ForeignKey(DoctorType, default=None, on_delete=models.CASCADE)
    symptoms = models.TextField(max_length=1000, default=None)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'


class Patient(User):
    diseases = models.ManyToManyField(Disease)
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Indicator(models.Model):
    type = models.CharField(max_length=30)
    diseases = models.ManyToManyField(Disease)


class Measurement(models.Model):
    type = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    testimony = models.IntegerField()
    comment = models.TextField(default=None)
    date = models.DateTimeField()


class Message(models.Model):
    DOCTOR = 'D'
    PATIENT = 'P'
    Author_choice = (
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient')
    )
    author = models.CharField('Author', choices=Author_choice, default=None, max_length=1)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    message = models.TextField(default=None)
    pub_date = models.DateTimeField(default=timezone.now)


class MeasurementFrequency(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    indicator = models.OneToOneField(Indicator, on_delete=models.CASCADE)
