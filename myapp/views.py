import json
import re
from django.http import HttpResponse, JsonResponse
from .models import Task, Project
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.</h1z
def index(request):
    return render(request, 'index.html')

def hello(request, user):
    return HttpResponse(f'<h1>Hello {user} </h1>')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects' : projects})

def tasks(request):
    task = Task.objects.all()
    return render(request, 'tasks.html', {'tasks' : task})

def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'create' : CreateNewTask() })
        
    else:
        Task.objects.create(tittle = request.POST['tittle'], description = request.POST['description'], projects_id = 2)
        return redirect('tasks')

def create_project(request):
    #Solo visualización de los proyectos
    if request.method == 'GET':
        return render(request, 'create_project.html', {'create' : CreateNewProject})
    #Creación de un nuevo proyecto    
    else:
        Project.objects.create(nombre = request.POST['nombre'])
        return redirect('projects')

def project_details(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(projects_id =id)
    return render(request, 'project_detail.html', {'project' : project, 'task' : task})
