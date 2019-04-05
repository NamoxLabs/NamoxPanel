from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.apps_review, name='apps'),
    url(r'^app/(?P<pk>\d+)/review/$', views.app_review, name='app-review'),
    url(r'^create/$', views.create_app, name='create-app'),
    url(r'^app/$', views.delete_app, name='delete-app')
]
