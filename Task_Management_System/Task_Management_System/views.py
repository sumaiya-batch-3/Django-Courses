from django.shortcuts import render
# from task.models import task

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')