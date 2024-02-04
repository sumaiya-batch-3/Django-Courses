from django.shortcuts import render 
from .forms import ExampleForm
  
# Create your views here. 
def home(request): 
    context ={} 
    # context['form']= InputForm() 
    context['form']= ExampleForm() 
    
    return render(request, "home.html", context)

