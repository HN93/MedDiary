from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from database.models import DoctorType


class SignUpFormDoctor(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    dateOfBirthday = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    city = forms.CharField(max_length=45)
    password = forms.CharField(max_length=30)
    phone_number = forms.IntegerField()
    type = forms.ModelChoiceField(queryset=DoctorType.objects.all())
    name_of_organisation = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'city', 'dateOfBirthday', 'gender',
                  'phone_number', 'first_name', 'last_name', 'type', 'name_of_organisation')
