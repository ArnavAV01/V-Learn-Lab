from django.urls import path
from . import views

urlpatterns = [
    path('semesters/',views.semesters,name='semesters'),
    path('subjects/',views.sem1sub,name='sem1sub'),
    path('subjects/',views.sem2sub,name='sem2sub'),
    path('subjects/',views.sem3sub,name='sem3sub'),
    path('subjects/',views.sem4sub,name='sem4sub'),
    path('subjects5sem/',views.sem5sub,name='sem5sub'),
    path('subjects/',views.sem6sub,name='sem6sub'),
    path('subjects/',views.sem7sub,name='sem7sub'),
    path('subjects/',views.sem8sub,name='sem8sub'),
]