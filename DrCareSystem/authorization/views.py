from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import DrAccount
from django.contrib.auth.decorators import login_required


def login(request):
    if(request.user.is_authenticated):
        return redirect('patients')
    if request.method == 'POST':
        username   = request.POST['username']
        password   = request.POST['password']
        person_ID  = request.POST['ID']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.person_ID==person_ID:
                auth.login(request, user)
                return redirect('patients')
            else:
                messages.info(request, 'Invalid ID')
                return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
