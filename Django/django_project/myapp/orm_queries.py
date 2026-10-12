
from django.db.models import Q, Avg
from myapp.models import Student


# Assessment 2 - Question 3
# Retrieve students aged 18 or above

def get_adult_students():
    return Student.objects.filter(age__gte=18)


# Example of OR filtering
def get_adult_students_or_rahul():
    return Student.objects.filter(
        Q(age__gte=18) | Q(name="Rahul")
    )


# Example of AND filtering
def get_adult_django_students():
    return Student.objects.filter(
        Q(age__gte=18) & Q(course__name="Django")
    )


# Assessment 2 - Question 4
# Calculate the average age of students

def get_average_student_age():
    return Student.objects.aggregate(
        average_age=Avg("age")
    )