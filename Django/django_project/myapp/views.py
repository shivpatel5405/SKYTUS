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

# Original FBV (kept for reference)
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'myapp/book_list.html', {
#         'books': books
#     })


# Assessment 3 :- Question 2 — Generic ListView Conversion (CBV)
from django.views.generic import ListView

class BookListView(ListView):
    model = Book                                    # Which model to query
    template_name = 'myapp/book_list.html'          # Which template to render
    context_object_name = 'books'                   # Variable name in template (matches FBV)