from django.shortcuts import render

# Assessment 1 :- create a view 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! Welcome to my Django project.")

# Assessment 2 :- adding dynamic url 

def student_detail(request, student_id):
    return HttpResponse(f"Student ID is: {student_id}")


# Assessment 3 :- Question 1 — Function-Based Views (FBV)
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {
        'books': books
    })