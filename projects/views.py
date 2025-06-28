from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from .models import Project
from .forms import ProjectCreateForm
from django.urls import reverse_lazy

class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'
    
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')