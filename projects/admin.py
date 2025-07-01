from django.contrib import admin

# Register your models here.
from .models import Category, Project, Task
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Task)