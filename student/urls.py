from django.urls import path
from . import views

urlpatterns = [
    path('semesters/',views.semesters,name='semesters'),
]