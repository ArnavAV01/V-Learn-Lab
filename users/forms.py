from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['enrollment_no', 'first_name', 'last_name', 'contact_number', 'branch', 'email', 'password1', 'password2']
