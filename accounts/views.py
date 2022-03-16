from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from accounts.models import *



def userregister(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login.html')

    return render(request, 'register.html', {'form':form})


def userlogin(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        data = request.POST
        u = data['username']
        p = data['password']
        user = authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home.html')
    return render(request, 'login.html', {'form':form})

def logout(request):

    return render(request,'home.html')