from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 5, 'lst' :['python', 'is', 'best'], 'birthday' : datetime.datetime.now(),'val' : '' , 'Courses' : [
        
        {
            'id' : 1,
            'name': 'Python',
            'fee': 5000
        },
        {
            'id' : 2,
            'name': 'Django',
            'fee': 7000
        },
        {
            'id' : 3,
            'name': 'C',
            'fee': 3000
        },

        ]}
    return render(request, 'home.html', d)
    # return render(request, 'home.html', {'author': 'Rahim', 'age': 20})