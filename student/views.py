from django.shortcuts import render

# Create your views here.
def semesters(requests):
    return render(requests, 'student/semesters.html')