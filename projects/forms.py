from django import forms
from .models import Project

field_attr = {'class': 'form-control'}
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category', 'title', 'description']
        widgets = {
            'category' : forms.Select(attrs=field_attr),
            'title' : forms.TextInput(attrs=field_attr),
            'description' : forms.Textarea(attrs=field_attr)
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category', 'title', 'status']
        widgets = {
            'category' : forms.Select(attrs=field_attr),
            'title' : forms.TextInput(attrs=field_attr),
            'status' : forms.Select(attrs=field_attr)
        }
