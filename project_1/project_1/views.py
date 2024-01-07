from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("this is home page")

# def contact(request):
#     return HttpResponse("This is contact page")


def home(request):
    return HttpResponse("This is  first_app page.")
def courses(request):
    return HttpResponse("This is  first_app/courses page.")

def courses(request):
    return HttpResponse("This is first app/about page.")