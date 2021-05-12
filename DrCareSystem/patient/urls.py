from django.urls import path, include
from . import views

urlpatterns = [
    path("patients", views.patients, name='patients'),
    path("getVisits", views.getVisits, name='getVisits'),
    path("getInfo", views.getInfo, name='getInfo'),
]
