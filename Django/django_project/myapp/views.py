from django.shortcuts import render

# Assessment 1 :- create a view 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! Welcome to my Django project.")
