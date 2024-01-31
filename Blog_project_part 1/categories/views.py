from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST': # user post request korecha
        category_form = forms.CategoryForm(request.POST) # user er post request data ekhana capture korlam
        if category_form.is_valid(): # post kora data gula amra valid ki na check koreteche
            category_form.save()# jodi data valid hoy tahole database e save korbo
            return redirect('add_category')# sob thik thakle take add author ei url e pathiye dibo.
        
    else:
        category_form = forms.CategoryForm() # user normally wedsite e gela blank form pabe
    return render(request, 'add_category.html', {'form' : category_form})