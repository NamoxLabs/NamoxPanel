from django.conf.urls import urls

from . import views

urlpatterns = [
    url(r'^$', views.details, name="details"),
    url(r'^profile$', views.profile, name="profile")



]
