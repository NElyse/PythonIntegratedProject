from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.test, name='testing'),
    path('students/', views.allstudents, name='allstudents'),
    path('studentDetail/<int:id>', views.studentDetails, name='studentDetails'),
    path('details/<int:pk>/', views.studentDetails, name='details'),
    path('studentRegister/', views.register, name='register'),
    path('Back/', views.allstudents, name='Back'),
    
    path('Back/', views.recordfunction, name='Back'),
   
]
