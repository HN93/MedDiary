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
from calendarOfDiseases import views as cof_views
from graphics import views as graph_views
from addDisease import views as add_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup_doctor/$', ac_views.signup_doctor, name='signup_doctor'),
    url(r'^signup_patient/$', ac_views.signup_patient, name='signup_patient'),
    url(r'^login/$', ac_views.log_in, name='log_in'),
    url(r'^logout/$', ac_views.logout, name='logout'),
    url(r'^patient/disease/measurement', cof_views.measurementCreateView, name='create_measurement'),
    url(r'^patient/disease/graph', graph_views.getGraph, name='graph'),
    url(r'^patient/disease/add', add_views.addDisease, name='add')

]
