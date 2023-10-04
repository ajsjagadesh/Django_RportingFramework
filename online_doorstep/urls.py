from django.contrib import admin
from django.urls import path, include
from . views import *

app_name = 'online_doorstep'  # Namespace for the app

urlpatterns = [
    path('', get_traking_id, name='online_doorstep'),
    path('get_data', doorstep),
]
