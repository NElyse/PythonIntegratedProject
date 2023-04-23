from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .models import StudentMovementManagement, Studentinfo
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registerForm, RecordForm


def test(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = registerForm()

    return render(request, 'RegisterForm.html', {'form': form})


def allstudents(request):
    students = Studentinfo.objects.all().values()
    template = loader.get_template('allstudents_info.html')

    context = {
        'student': students,
    }
    return HttpResponse(template.render(context, request))
  
def studentDetail(request):
    students = Studentinfo.objects.all().values()
    template = loader.get_template('studentDetails.html')

    context = {
        'student': students,
    }
    return HttpResponse(template.render(context, request))





def selectDataToInsertMovementReport(request):
    students = Studentinfo.objects.all().filter(Regno='20RP11582').values()

    template = loader.get_template('MoveForm.html')
    context = {
        'student': students,
    }
    return HttpResponse(template.render(context, request))


def recordMovement(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = registerForm()
    return render(request, 'MoveForm.html', {'form': form})


def reportData(request):
    students = StudentMovementManagement.objects.all().filter(
        Regno='20RP11582').order_by('time_in,time_out').values()
    template = loader.get_template('studentMoveDetails.html')
    context = {
        'student': students,
    }
    return HttpResponse(template.render(context, request))


def reportDataAll(request):
    students = StudentMovementManagement.objects.all().order_by(
        'time_in,time_out').values().values()
    template = loader.get_template('studentMoveDetails.html')

    context = {
        'student': students,
    }
    return HttpResponse(template.render(context, request))




def loginFunction(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['Password']
        user = authenticate(request, Username=Username, Password=Password)
        if user is not None:
            login(request, user)
            return redirect('studentsAll')
        else:
            error_message = "Invalid username or password"
            return render(request, 'Login.html', {'error_message': error_message})
    else:
        return render(request, 'Login.html')
    

def logoutFunction(request):
    logout(request)
    return redirect('loginFunction')




