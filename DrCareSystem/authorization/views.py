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
        msg = checkLogin(username)
        if(msg):
            messages.info(request, msg)
            return redirect('/')
        password   = request.POST['password']
        msg = checkPw(password)
        if(msg):
            messages.info(request, msg)
            return redirect('/')
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

def checkLogin(login):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    if(len(login)<6 or len(login)>8):
        return "Username must be 6-8 chars"
    counter = 0
    for c in login:
        if c in digits:
            counter+=1
    if counter >2 :
        return "Username can contain maximum two digits"

def checkPw(pw):
    special = ["!","@","#","$","%","^","&","*"]
    if(len(pw)<8 or len(pw)>10):
        return "Password must be 8-10 chars"
    if  not (any(c.isalpha() for c in pw) == True and  any(c.isdigit() for c in pw) == True and len(list(filter(lambda x: x in special,pw)))>0):
        return "Password must be alphanumeric and atleast one special symbol [!,@,#,$,%,^,&,*]"