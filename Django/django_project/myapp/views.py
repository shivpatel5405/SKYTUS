from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Everyone ! Welcome to my Django project.") 

def student_detail(request, student_id):
    return HttpResponse(f"Student ID is: {student_id}")     