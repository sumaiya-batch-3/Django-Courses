from django.shortcuts import render

def index(request):

#     value = [
#     {'name': 'zed', 'age': 19},
#     {'name': 'amy', 'age': 22},
#     {'name': 'joe', 'age': 31},
# ]
    value = "Sumaiya Sharmin"
 
    return render(request, 'index.html', {'value': value})