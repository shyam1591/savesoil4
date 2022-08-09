from .models import Photocontest 
from django import forms
from django.forms import ModelForm



class Photocontestform(ModelForm):
    """Contest form"""
    class Meta:
        model = Photocontest
        fields = ('name','email','image')