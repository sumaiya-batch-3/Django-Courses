from django.shortcuts import render

# C:\python_django\project_2\templates
def index(request):
    return render(request,'index.html')