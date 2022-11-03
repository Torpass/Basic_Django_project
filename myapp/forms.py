from cProfile import label
from mailbox import NoSuchMailboxError
from django import forms

class CreateNewTask(forms.Form):
    tittle = forms.CharField(label = 'Taks title', max_length=50, widget=forms.TextInput(attrs={'class' :'input'}) )
    description = forms.CharField(label = 'Description',widget=forms.Textarea(attrs={'class' :'input'}))

class CreateNewProject(forms.Form):
    nombre = forms.CharField(label= 'Name of the project', max_length=30, widget=forms.TextInput(attrs={'class' :'input'}))