from django import forms
from .models import Project

field_attr = {'class': 'form-control'}
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category', 'title', 'description']
        widgets = {
            'category' : forms.Select(),
            'title' : forms.TextInput(),
            'description' : forms.Textarea()
        }