from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.test, name='testing'),
    path('studentRegister/',views.register, name='register'),
    
    path('studentsAll/', views.allstudents, name='allstudents'),
    path('studentDetail/', views.studentDetail, name='studentDetails'),
    path('SelectDatarecord/', views.selectDataToInsertMovementReport, name='SelectDataTorecord'),
    path('recordMovement/', views.recordMovement, name='recordMovement'),
    path('viewReport/', views.reportData, name='viewReportForOne'),
    path('viewReportAll/', views.reportDataAll, name='viewReportForAll'),
    path('login/', views.loginFunction, name='login'),
    path('logout/', views.logoutFunction, name='logout'),
   
]
