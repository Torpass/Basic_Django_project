from os import O_NDELAY
from pyexpat import model
import string
from django.db import models

#Los models son los modelos de las tablas de datos que vayas a necesitar en tu aplicación. 
#Estos funcionan muy parecido a las clases, los atributos son los valores que van a ser agregados a esas tablas y no continen métodos
#También estas tablas pueden estar relacionadas entre si, recibiendo valores de otras clases


# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Task(models.Model):
    tittle = models.CharField(max_length = 50)
    description = models.TextField()
    projects =  models.ForeignKey(Project, on_delete = models.CASCADE) 
    #ForeignKey se usa para relacionar tabalas... 
    #on_delete se usa para saber que hacer si el modelo con el que esta relacionado es eliminado...   
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle + ' - ' + self.projects.nombre