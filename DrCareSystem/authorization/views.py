from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import DrAccount
from django.contrib.auth.decorators import login_required

# def login(request):
#     if(request.user.is_authenticated):
#         return redirect('/')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect('login')

#     else:
#         return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
        username   = request.POST['username']
        password   = request.POST['password']
        person_ID  = request.POST['ID']
        user = auth.authenticate(person_ID=person_ID,username=username, password=password)
        if user is not None:
            if user.person_ID==person_ID:
                auth.login(request, user)
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