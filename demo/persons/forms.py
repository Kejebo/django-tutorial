from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields='__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
        }