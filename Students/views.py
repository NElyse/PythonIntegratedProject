from django.http import HttpResponse
from django.template import loader
from .models import Studentinfo
from django.shortcuts import render, redirect, get_object_or_404
from .forms import registerForm, RecordForm
from django.http import HttpResponseRedirect


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
  students = get_object_or_404(Studentinfo, id=id)
  template = loader.get_template('studentDetails.html')
  
  context = {
    'student': students,
  }
  return HttpResponse(template.render(context, request))






def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
           form.save()
           
        
        return redirect('students')
    else:
        form = registerForm()
 
    return render(request, 'RegisterForm.html', {'form': form})
  
  
  
def recordfunction(request):
  if request.method == 'POST':
      form = RecordForm(request.POST)
      if form.is_valid():
          form.save()
      
      return HttpResponseRedirect('/students/')
  else:
      form = registerForm()
  return render(request, 'MoveForm.html', {'form': form})
  



  
  

