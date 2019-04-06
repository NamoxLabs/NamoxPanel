from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import AppForm


def apps_review(request):
    print("apps_review")
    pass


def app_review(request):
    print("app_review")
    pass


def create_app(request):
    #app_form=AppForm(data=request.POST or None)
    app_form=AppForm(request.POST or None)
    if app_form.is_valid():
        app_form.save()
    else:
        # if a GET (or any other method) we'll create a blank form
        app_form = AppForm()
    ctx = {'app_form': ''}
    
    return TemplateResponse(request, 'app/create_app.html', ctx)


def delete_app(request):
    print("delete_app")
    pass
