from django import forms
from . import models
 
class UniversityForm(forms.ModelForm):
    class Meta:
        model = models.University
        fields = ['full_name', 'short_name', 'founded_date']
        widgets = {
            'founded_date': forms.DateInput(attrs={'type': 'date'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['full_name', 'birth_date', 'university', 'enrollment_year']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }