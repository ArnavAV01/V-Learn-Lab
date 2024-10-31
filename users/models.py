from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    enrollment_no = models.CharField(max_length=20, unique=True) 
    email = models.EmailField(unique=True)
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
     
    USERNAME_FIELD = 'enrollment_no'  
    REQUIRED_FIELDS = ['email']  
