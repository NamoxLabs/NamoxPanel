from django.conf.urls import include, url
# from django.urls import include, path

from . import views


urlpatterns = [
    url(r'^', views.home, name='home'),
]
