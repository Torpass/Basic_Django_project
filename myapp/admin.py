from django.contrib import admin

from myapp.views import projects
from .models import Project, Task
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
