from django.core import validators
from django import forms
from .models import EducatorRecord
from datetime import date

class EducatorRegistration(forms.ModelForm):
    class Meta:
        model=EducatorRecord
        fields=['FirstName','MiddleName','LastName','OutDate','InDate','ClassName','MobNo']
        widget={
            'FirstName': forms.TextInput(attrs={'class':'form-control'}),
            'MiddleName': forms.TextInput(attrs={'class':'form-control'}),
            'LastName': forms.TextInput(attrs={'class':'form-control'}),
            'InDate': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'OutDate': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'ClassName': forms.TextInput(attrs={'class':'form-control'}),
            'MobNo': forms.TextInput(attrs={'class':'form-control'}),
        }
