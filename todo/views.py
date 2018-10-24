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
            email_domain = username[username.find('@')+1:]
            user = User.objects.create_user(username=username, email=username, password=password, first_name=first_name, last_name=last_name)
            new_group, created = Group.objects.get_or_create(name=email_domain)
            if created:
                user.is_staff = True
                user.is_active = True
            else:
                user.is_staff = False
                user.is_active = False
            user.save()            
            new_group.user_set.add(user)
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
    context = {}
    if user.is_authenticated:
        context['name'] = user.first_name
        if user.is_staff:
            user_group = user.groups.all()[0]
            #all_users = User.objects.all().filter(groups__name=user_group)
            all_users = user_group.user_set.all().exclude(username=user).filter(is_active=False)
            print(all_users)
            context['all_users'] = [user for user in all_users]
        return render(request, 'dashboard.html', context=context)
    else:
        return render(request, 'home.html')

@login_required
def approve(request, user_id=None):
    user = request.user
    if user.is_authenticated:
        user_2b_approved = User.objects.filter(id=user_id)[0]
        user_2b_approved.is_active = True
        user_2b_approved.save()
        return HttpResponseRedirect('/dashboard/')
