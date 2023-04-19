from django.http import HttpResponse
from django.template import loader
from .models import Studentinfo
from django.shortcuts import render, redirect
from .forms import registerForm


def test(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())



def allstudents(request):
  students = Studentinfo.objects.all().values()
  template = loader.get_template('allstudents_info.html')
  
  context = {
    'student': students,
  }
  return HttpResponse(template.render(context, request))




def studentDetails(request):
  # students = Studentinfo.objects.all().values()
  students = Studentinfo.objects.all().filter(id=3)
  template = loader.get_template('studentDetails.html')
  
  context = {
    'student': students,
  }
  return HttpResponse(template.render(context, request))






def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            Student = Studentinfo.objects.create_user(
                nid=form.cleaned_data['nid'],
                midle_name=form.cleaned_data['midle_name'],
            )
            form.save()
    else:
        form = registerForm()
    return render(request, 'RegisterForm.html', {'form': form})
  
  

