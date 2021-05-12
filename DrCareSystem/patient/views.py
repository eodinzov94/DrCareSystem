from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
@login_required
def patients (request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

@login_required
def getVisits (request):
    if request.method == 'POST':
        id      = request.POST['id']
        patient = Patient.objects.get(id=id)
        visits  = Visit.objects.filter(patient=patient)
        return render(request, 'patientinfo.html', {'visits': visits,'patient':patient})
    else:
        return redirect('patients')

@login_required
def getInfo(request):
    if request.method == 'POST':
        id      = request.POST['id']
        patient = Patient.objects.get(id=id)
        results = patient.health_param
        quest   = patient.questionnaire
        return render(request, 'medinfo.html', {'results': results,'quest': quest})
    else:
        return redirect('patients')