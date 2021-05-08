from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def patients (request):
    return render(request, 'patients.html')
