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
def newVisit (request): #TODO: Add functionality
    if request.method == 'POST':
        id      = request.POST['id']
        patient = Patient.objects.get(id=id)
        return render(request, 'newVisit.html', {'patient':patient})
        

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


@login_required
def newPatient(request): #TODO: make error appear on screen.
    if request.method == 'POST':
        fullName = request.POST.get('fullname')
        personID = request.POST.get('personid')
        tel = request.POST.get('tel')
        gender = request.POST.get('gender')
        age = request.POST.get('age')

        if len(fullName) < 4:
            messages.info(request, 'Name too short!')
            return redirect('newPatient')
        if len(personID) != 9:
            messages.info(request, 'ID Must be 9 digits long!')
            return redirect('newPatient')
        if len(tel) != 10:
            messages.info(request, 'Phone must be 10 digits long!')
            return redirect('newPatient')
        if age < 0 or age > 140:
            messages.info(request, 'Illegal age!')
            return redirect('newPatient')        

        newP = Patient(
            fullName=fullName,
            personID=personID,
            tel=tel,
            gender=gender,
            age=age,
        )

        newP.save()
        return redirect('patients')
    else:
        return render(request, 'newPatient.html')