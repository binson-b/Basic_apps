from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            User.objects.create_user(username=username, email=username, password=password)
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
            User.objects.create_user(username=username, email=username, password=password)
            return HttpResponseRedirect('/thanks/')
            
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})