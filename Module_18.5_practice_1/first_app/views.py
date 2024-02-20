from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')  
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()

    return render(request, "register.html", {'form': register_form,'type':'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request,data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password = user_pass)
            if user is not None:
                messages.success(request,'Login Successfully')  
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Login information wrong')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form, 'type':'Login'})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('user_login')

def user_logout(request):
    logout(request)
    return redirect('user_login')