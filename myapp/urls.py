from multiprocessing.spawn import import_main_path
from django.urls import path
from django.views import View
from . import views

urlpatterns = [
    path ('', views.index, name= 'index'),
    path ('about/', views.about, name= 'about'),
    path ('hello/<user>/', views.hello, name= 'user'),
    path ('tasks/', views.tasks, name= 'tasks'),
    path ('projects/', views.projects, name= 'projects'),
    path ('projects/<int:id>', views.project_details, name= 'd_project'),
    path ('create_new_tasks/', views.create_tasks, name= 'c_tasks'),
    path ('create_new_project/', views.create_project, name= 'c_project'),
]
