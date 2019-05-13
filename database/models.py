from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    second_name = models.CharField('second_name', null=True, blank=True, max_length=50)
    date_of_birthday = models.DateField('date_of_birthday', null=True, blank=True)
    gender = models.CharField('gender', choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    city = models.CharField('city', max_length=45, null=True, blank=True)
    phone_number = models.IntegerField('phone_number', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class DoctorType(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'DoctorType'
        verbose_name_plural = 'DoctorTypes'

    def __str__(self):
        return '%s' % self.name


class Doctor(Profile):
    type = models.ForeignKey(DoctorType, on_delete=models.CASCADE, null=True, blank=True)
    name_of_organisation = models.CharField(max_length=50, null=True, blank=True)
    license = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s' % self.user.first_name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Disease(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    doctorType = models.ForeignKey(DoctorType, null=True, blank=True, on_delete=models.CASCADE)
    symptoms = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'


class Patient(Profile):
    diseases = models.ManyToManyField(Disease, null=True, blank=True)
    doctors = models.ManyToManyField(Doctor, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    dms = models.IntegerField(null=True, blank=True)
    oms = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.user.first_name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Indicator(models.Model):
    type = models.CharField(max_length=30, null=True, blank=True)
    diseases = models.ManyToManyField(Disease)

    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'


class Measurement(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True, blank=True)
    testimony = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    doctor_comment = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'


class ExpectedValue(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField('gender', choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
