from django.db.models.signals import post_save
from django.dispatch import receiver
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
    first_name = models.CharField(max_length=45, null=False, blank=False)
    last_name = models.CharField(max_length=45, null=False, blank=False)
    dateOfBirthday = models.DateField(blank=False)
    gender = models.CharField('gender', choices=GENDER_CHOICES, max_length=1, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    city = models.CharField(max_length=45, default=None)
    mail = models.EmailField(max_length=100, default=None)
    password = models.CharField(max_length=30, null=False, blank=False, default=None)
    phone_number = models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, default=None)

    class Meta:
        abstract = True


class DoctorType(models.Model):
    name = models.CharField(max_length=20, null=True, blank=False)

    class Meta:
        verbose_name = 'DoctorType'
        verbose_name_plural = 'DoctorType'


class Doctor(Profile):
    type = models.ForeignKey(DoctorType, on_delete=models.CASCADE, null=True)
    name_of_organisation = models.CharField(max_length=50, null=True, blank=False)

    @receiver(post_save, sender=User)
    def new_user(sender, instance, created, **kwargs):
        if created:
            Doctor.objects.create(user=instance)
        instance.doctor.save()

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


class Patient(Profile):
    diseases = models.ManyToManyField(Disease)
    doctors = models.ManyToManyField(Doctor)
    height = models.IntegerField(default=None)
    weight = models.IntegerField(default=None)

    @receiver(post_save, sender=User)
    def new_user(sender, instance, created, **kwargs):
        if created:
            Patient.objects.create(user=instance)
        instance.patient.save()

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Indicator(models.Model):
    type = models.CharField(max_length=30)
    diseases = models.ManyToManyField(Disease)
    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'


class Measurement(models.Model):
    type = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    testimony = models.IntegerField()
    comment = models.TextField(default=None)
    date = models.DateTimeField()


class Message(models.Model):
    from_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_whom', default=None)
    to_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_whom', default=None)
    message = models.TextField(default=None)
    pub_date = models.DateTimeField(default=timezone.now)


class MeasurementFrequency(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    frequency = models.IntegerField(default=2)
