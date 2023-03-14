from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signupaccount(request):
    if (request.method) == 'GET':
        return render(request, 'signup.html', {'form': CustomUserCreationForm})
    elif(request.POST['password1'] == request.POST['password2']):
        try:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('show')
        except IntegrityError:
            return render(request, 'signup.html', {'form': CustomUserCreationForm, 'error': 'Username already exists. Choose new username'})
    else:
        return render(request, 'signup.html', {'form': CustomUserCreationForm, 'error':'Passwords do not match'})

def logoutaccount(request):
    logout(request)
    return redirect('mainpage')

def loginaccount(request):
    if (request.method == 'GET'):
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if(user is None):
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Username and Password do not match'})
        else:
            login(request, user)
            return redirect('show')