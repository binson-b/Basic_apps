from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm


# Create your views here.

def home(request):
    pass
    return render(request, 'home.html')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            #Group.objects.
            user = User.objects.create_user(username=username, email=username, password=password, first_name=first_name, last_name=last_name, active=False)
            print(user)
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
            
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

@login_required
def user_dashboard(request):
    user = request.user
    print(dir(user))
    if user.is_authenticated:
        return render(request, 'dashboard.html', {'name':user.first_name})
    else:
        return render(request, 'home.html')