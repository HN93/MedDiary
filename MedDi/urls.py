"""MedDi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from accounts import views as ac_views
from calendarOfDiseases import views as cod_views
from graphics import views as graph_views
from addDisease import views as add_views
from doctor import views as doctor_views
from patient import views as pv

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup_doctor/$', ac_views.signup_doctor, name='signup_doctor'),
    url(r'^signup_patient/$', ac_views.signup_patient, name='signup_patient'),
    url(r'^signup/$', ac_views.signup, name='signup'),
    url(r'^login/$', ac_views.log_in, name='log_in'),
    url(r'^logout/$', ac_views.logout, name='logout'),
    url(r'^patient/disease/measurement', cod_views.measurementCreateView, name='create_measurement'),
    url(r'^patient/disease/graph', graph_views.getGraph, name='graph'),
    url(r'^patient/disease/add', add_views.addDisease, name='add'),
    url(r'^doctor/patient/info', doctor_views.getPatientInfo, name='patient_info'),
    url(r'^doctor/patient/add', doctor_views.addPatient, name='add_patient'),
    url(r'^doctor/patient/graph', graph_views.get_graph_doctor, name='graph'),
    url(r'^doctor/patient/delete', doctor_views.deletePatient, name='delete_patient'),
    url(r'^patient/profile/', pv.getPatientProfile, name='patient_profile'),
    url(r'^patient/passchange', pv.passchange),
    url(r'^doctor/profile', doctor_views.doctorProfile, name='doctor_profile'),
    url(r'^doctor/passchange', doctor_views.passchange, name='passchange')

]
