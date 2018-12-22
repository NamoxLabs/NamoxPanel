from django.shortcuts import render
from django.http      import HttpResponse
from django.template.response import TemplateResponse

from . import forms

# Create your views here.

# PROYECTS VIEWS
def listProject( request ):
    pass

def createProject( request ):
    user = request.user
    create_project = forms.ProjectForm(data=request.POST or None)
    if create_project.is_valid():
        project = create_project.save(commit=False)
        project.created_by = request.user
        project.save()

        #return TemplateResponse("projects/overview.html")
    ctx = {'create_project': create_project}
    return TemplateResponse(request, 'projects/create_project.html', ctx)

def editProject( request ):
    pass

def deleteProject( request ):
    pass

# ENTITYS VIEWS
def listEntity( request ):
    pass

def createEntity( request ):
    pass

def editEntity( request ):
    pass

def deleteEntity( request ):
    pass

# ATTRIBUTS VIEWS
def listAttribut( request ):
    pass

def createAttribut( request ):
    pass

def editAttribut( request ):
    pass

def deleteAttribut( request ):
    pass