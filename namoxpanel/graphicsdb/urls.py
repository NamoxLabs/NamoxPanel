from django.conf.urls import url, include

from . import views

urlpatterns = [
    url( r'^$', views.listProject, name = 'list_proyects' ),
    url( r'^create/$', views.createProject, name = 'create_proyect'),
    url( r'^edit/$', views.editProject, name = 'edit_proyect'),
    url( r'^delete/$', views.deleteProject, name = 'delete_proyect'),
]

"""
url( r'^attributs/$', listAttribut, name = 'list_attributs' ),
url( r'^attributs/create/$', createAttribut, name = 'create_attributs'),
url( r'^attributs/edit/$', editAttribut, name = 'edit_attributs'),
url( r'^attributs/delete/$', deleteAttribut, name = 'delete_attributs'),

url( r'^entitys/$', listEntity, name = 'list_entitys' ),
url( r'^entitys/create/$', createEntity, name = 'create_entitys' ),
url( r'^entitys/edit/$', editEntity, name = 'edit_aentitys' ),
url( r'^entitys/delete/$', deleteEntity, name = 'delete_entitys' ),
"""