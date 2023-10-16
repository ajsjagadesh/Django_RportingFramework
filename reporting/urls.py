from django.contrib import admin
from django.urls import path, include
from . views import *

app_name = 'reporting'  # Namespace for the app

urlpatterns = [
    path('', report, name='reporting'),
    path('data', report_procces, name='formdata'),
    path('reports', report_home, name="report_home"),
    path('download', download, name="download_file")
]
