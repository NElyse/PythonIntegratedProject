
from django import forms
from .models import StudentMovementManagement, Studentinfo
from .validator import validate_phone_number,validate_national_id ,registration_number_validator



class registerForm(forms.ModelForm):
    class Meta:
        model = Studentinfo
        phone_number = forms.CharField(validators=[validate_phone_number])
        nid = forms.CharField(validators=[validate_national_id])
        Regno = forms.CharField(validators=[registration_number_validator])
        
        fields = ['Regno', 'first_name','last_name', 'nid', 'email', 'phone_number']
        
        



class RecordForm(forms.ModelForm):
    class Meta:
        model = StudentMovementManagement

        fields = ['Regno', 'first_name','last_name', 'phone_number']


       