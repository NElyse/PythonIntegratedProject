from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

def index(request):
    users = User.objects.all()
    return render(request,'test.html',{"users":users})