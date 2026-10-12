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
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book                                    # Which model to query
    template_name = 'myapp/book_list.html'          # Which template to render
    context_object_name = 'books'                   # Variable name in template (matches FBV)


# Assessment 3 :- Question 3 — Form Creation & Redirects (CreateView)

class BookCreateView(CreateView):
    model = Book                                    # Which model to create
    fields = ['title', 'author']                    # Which fields to show in the form
    template_name = 'myapp/book_form.html'          # Which template to render
    success_url = reverse_lazy('book_list')         # Redirect to book list after successful submission  


 # Assessment 3 :- Question 4 — Context Customization
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context (includes 'books')
        context['total_books'] = Book.objects.count() # Add total count of books
        context['heading'] = 'Our Book Collection'    # Add a dynamic heading
        return context