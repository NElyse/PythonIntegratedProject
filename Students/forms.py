import string
from django import forms
from .models import StudentMovementManagement, Studentinfo
from django.core.exceptions import ValidationError


class registerForm(forms.ModelForm):
    class Meta:
        model = Studentinfo

        fields = ['Regno', 'first_name','last_name', 'nid', 'email', 'phone_number']
        






class RecordForm(forms.ModelForm):
    class Meta:
        model = StudentMovementManagement

        fields = ['Regno', 'first_name','last_name', 'phone_number']


       