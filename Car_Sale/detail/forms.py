from django import forms
from .models import Car,Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['car']