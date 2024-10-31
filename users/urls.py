from django.urls import path
from . import views

urlpatterns = [
    path('register-student/', views.register_student, name='register-student'),
    path('register-faculty/', views.register_faculty, name='register-faculty'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]