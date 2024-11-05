from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    enrollment_no = models.CharField(max_length=20, unique=True) 
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)  # New field
    last_name = models.CharField(max_length=30)   # New field
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'enrollment_no'  
    REQUIRED_FIELDS = ['email']  
