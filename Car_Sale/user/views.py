from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from . import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import DeleteView
# Create your views here.

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request,'account created successfully')  
               return redirect('login')
        else:
           form = forms.RegistrationForm()
        return render(request, "register.html", {'form': form,'type':'Sign'})
    else:
     return redirect('profile')  
    
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request,data = request.POST)
            if form.is_valid():
              user_name = form.cleaned_data['username']
              user_pass = form.cleaned_data['password']
              user = authenticate(username=user_name,password = user_pass)
              if user is not None:
                messages.success(request,'Login successfully')  
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Login information wrong')
                return redirect('register')
        else:
              form = AuthenticationForm()

        return render(request,'register.html',{'form':form, 'type':'Log'})
        
    else:
     return redirect('profileUpdate')
  
def about(request):
    return render(request,'about.html')
    

def user_logout(request):
    logout(request)
    return redirect('login')

def password_change(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'pass_change.html', {'form': form})
    
@login_required
def profileUpdate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.UserUpdateData(request.POST,instance=request.user )
            if form.is_valid():
               form.save()
               messages.success(request,'Account updated successfully')  
            #    return redirect('')
            print(form.cleaned_data)
        else:
           form = forms.UserUpdateData(instance=request.user)
        return render(request, "profile_update.html", {'form': form})
    else:
     return redirect('register')  
    



