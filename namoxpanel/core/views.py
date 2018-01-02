from django.template.response import TemplateResponse
from django.shortcuts import render

#from ..apps.models import App

def home(request):
    ctx = {'apps': apps}
    return TemplateResponse(request, 'home.html',
    ctx)
