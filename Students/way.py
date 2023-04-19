from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.test, name='testing'),
    path('students/', views.allstudents, name='allstudents'),
    path('studentDetail/', views.studentDetails, name='studentDetails'),
    path('studentRegister/', views.register, name='register'),
]