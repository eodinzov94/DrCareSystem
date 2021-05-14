from django.urls import path, include
from . import views

urlpatterns = [
    path("patients", views.patients, name='patients'),
    path("getVisits", views.getVisits, name='getVisits'),
    path("getInfo", views.getInfo, name='getInfo'),
    path("newPatient",views.newPatient,name='newPatient'),
    path("newVisit",views.newVisit,name='newVisit'),
    path("updateQuest",views.updateQuest,name='updateQuest'),
]
