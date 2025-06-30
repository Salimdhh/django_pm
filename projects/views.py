from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task
from .forms import ProjectCreateForm, ProjectUpdateForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/list.html'
    paginate_by = 6
    def get_queryset(self):
        query_set = super().get_queryset()
        where ={}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project/update.html'
    success_url = reverse_lazy('Project_list')
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    
    def get_success_url(self):
        return reverse_lazy('Project_list')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['project', 'description']
#    http_method_names = ['POST']
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['is_completed']
#    http_method_names = ['POST']
    
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])

