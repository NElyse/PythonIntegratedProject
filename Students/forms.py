import string
from django import forms
from .models import Studentinfo
from django.core.exceptions import ValidationError


class registerForm(forms.ModelForm):
    class Meta:
        model = Studentinfo

        fields = ['Regno', 'first_name','last_name', 'nid', 'email', 'phone_number']

    class ContactForm(forms.Form):

        def clean(self):
            cleaned_data = super().clean()

            nida = cleaned_data.get('nid')

            if string.count(nida) != 16:
                raise forms.ValidationError('National Id  do not match')

            midle_nme = cleaned_data.get('midle_name')

            forms.NullBooleanField(midle_nme, required=False)
            Regn = cleaned_data.get('Regno')

            forms.NullBooleanField(Regn, required=False)
