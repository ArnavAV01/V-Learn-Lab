from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from .models import User

# Register Student
def register_student(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.is_student = True  # Mark as student
            student.username = student.enrollment_no  # Set enrollment_no as username
            student.save()
            messages.success(request, 'Student account has been created successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Error creating student account. Please check the form for issues.')
    else:
        form = RegisterUserForm()
    
    return render(request, 'users/register_student.html', {'form': form})

# Register Faculty
def register_faculty(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            faculty = form.save(commit=False)
            faculty.is_faculty = True  # Mark as faculty
            faculty.username = faculty.enrollment_no  # Set enrollment_no as username
            faculty.save()
            messages.success(request, 'Faculty account has been created successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Error creating faculty account. Please check the form for issues.')
    else:
        form = RegisterUserForm()
    
    return render(request, 'users/register_faculty.html', {'form': form})

    
# Login a User
def login_user(request):
    if request.method == 'POST':
        enrollment = request.POST.get('enrollment_no')
        password = request.POST.get('password')
        
        # Authenticate using enrollment_no
        user = authenticate(request, username=enrollment, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid enrollment number or password.')
    
    return render(request, 'users/login.html')

# Logout a user
def logout_user(request):
    logout(request)
    messages.info(request,'Your session has ended.')
    return redirect('login') 