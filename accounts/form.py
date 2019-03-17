from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from database.models import DoctorType
from database.models import Doctor
from database.models import Patient


class SignUpFormDoctor(UserCreationForm):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    date_of_birthday = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    city = forms.CharField(max_length=45)
    phone_number = forms.IntegerField()
    name_of_organisation = forms.CharField(max_length=50)
    type = forms.ModelChoiceField(queryset=DoctorType.objects.all())
    email = forms.EmailField();

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birthday', 'gender',
                  'city', 'phone_number', 'name_of_organisation', 'type', 'email')


class SignUpFormPatient(UserCreationForm):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    date_of_birthday = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    city = forms.CharField(max_length=45)
    phone_number = forms.IntegerField()
    email = forms.EmailField(max_length=254)
    height = forms.IntegerField()
    weight = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birthday', 'gender',
                  'city', 'phone_number', 'email', 'height', 'weight')
