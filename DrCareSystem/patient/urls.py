from django.urls import path, include
from . import views

urlpatterns = [
    path("patients", views.patients, name='patients'),
]