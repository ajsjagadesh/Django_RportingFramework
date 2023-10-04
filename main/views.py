from django.shortcuts import render

# Create your views here.

__author__ = 'ajagadish.nayak'

def home(req):
    return render(req, 'home.html')

