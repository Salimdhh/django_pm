from django.contrib import admin
from django.db.models import Count

# Register your models here.
from .models import Category, Project, Task
admin.site.register(Category)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'user', 'category', 'created_at', 'tasks_count']
    list_per_page = 20
    list_select_related = ['category', 'user']
    list_editable = ['title', 'status', 'user', 'category']
    list_display_links = ['id'] 
    def tasks_count(self, obj):
        return obj.task_count
    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(task_count=Count('task'))
        return query


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_display_links = ['id']