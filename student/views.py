from django.shortcuts import render

# Create your views here.
def semesters(requests):
    return render(requests, 'student/CSE-AIML/semesters.html')


def sem8sub(requests):
    return render(requests,'student/CSE-AIML/semester 8/subjects.html')

def sem7sub(requests):
    return render(requests,'student/CSE-AIML/semester 7/subjects.html')

def sem6sub(requests):
    return render(requests,'student/CSE-AIML/semester 6/subjects.html')

def sem5sub(requests):
    return render(requests,'student/CSE-AIML/semester 5/subjects5sem.html')

def sem4sub(requests):
    return render(requests,'student/CSE-AIML/semester 4/subjects.html')

def sem3sub(requests):
    return render(requests,'student/CSE-AIML/semester 3/subjects.html')

def sem2sub(requests):
    return render(requests,'student/CSE-AIML/semester 2/subjects.html')

def sem1sub(requests):
    return render(requests,'student/CSE-AIML/semester 1/subjects.html')