from django.conf.urls import url, include

from graphicsdb.views import listProyect, listAttribut, listEntity
from graphicsdb.views import createProyect, createAttribut, createEntity
from graphicsdb.views import editProyect, editAttribut, editEntity
from graphicsdb.views import deleteProyect, deleteAttribut, deleteEntity



urlpatterns = [
    url( r'^proyects$', listProyect, name = 'list_proyects' ),
    url( r'^proyects/create/$', createProyect, name = 'create_proyect'),
    url( r'^proyects/edit/$', editProyect, name = 'edit_proyect'),
    url( r'^proyects/delete/$', deleteProyect, name = 'delete_proyect'),

    url( r'^attributs/$', listAttribut, name = 'list_attributs' ),
    url( r'^attributs/create/$', createAttribut, name = 'create_attributs'),
    url( r'^attributs/edit/$', editAttribut, name = 'edit_attributs'),
    url( r'^attributs/delete/$', deleteAttribut, name = 'delete_attributs'),

    url( r'^entitys/$', listEntity, name = 'list_entitys' ),
    url( r'^entitys/create/$', createEntity, name = 'create_entitys' ),
    url( r'^entitys/edit/$', editEntity, name = 'edit_aentitys' ),
    url( r'^entitys/delete/$', deleteEntity, name = 'delete_entitys' ),
]