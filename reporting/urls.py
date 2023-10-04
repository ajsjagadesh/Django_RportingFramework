from django.contrib import admin
from django.urls import path, include
from . views import *

app_name = 'reporting'  # Namespace for the app

urlpatterns = [
    path('', report, name='reporting'),
    path('data', form_input, name='formdata')
]
