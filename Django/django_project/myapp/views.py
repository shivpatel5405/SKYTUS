from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Everyone ! Welcome to my Django project.") 
