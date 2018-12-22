# IMPORTS DJANGO
from django import forms
from django.utils.translation import pgettext_lazy

# IMPORTS APP
from . import models

class ProjectForm( forms.ModelForm ):
    class Meta:
        model  = models.Project
        fields = [
            'name'
        ]

        labels = {
            'name'       : 'Name'
        }

        widgets = {
            'name'       : forms.TextInput( attrs = { 'class': '' } )
        }


class EntityForm( forms.ModelForm ):

    class Meta:

        model  = models.Entity
        fields = [
            'name'
        ]

        labels = {
            'name'       : 'Name'
        }

        widgets = {
            'name'       : forms.TextInput( attrs = { 'class' : '' } ),
        }


"""
class AttributeForm( forms.ModelForm ):

    class Meta:

        model  = Attribute
        fields = [
            'id_entity',
            'name',
            'type',
            'is_null',
            'is_auto_increment',
            'is_unique',
            'is_primary_key',
            'is_indice',
            'register',
            'last_update'
        ]

        labels = {
            'id_entity'        : 'Entity',
            'name'             : 'Name',
            'type'             : 'Type',
            'is_null'          : 'Is null',
            'is_auto_increment': 'Is auto incremental',
            'is_unique'        : 'Is unique',
            'is_primary_key'   : 'Is primary key',
            'is_indice'        : 'Is indice',
            'register'         : 'Register',
            'last_update'      : 'Last update'
        }

        widgets = {
            'id_entity'        : forms.Select( attrs = { 'class' : '' } ),
            'name'             : forms.TextInput( attrs = { 'class' : '' } ),
            'type'             : forms.Select( attrs = { 'class' : '' } ),
            'is_null'          : forms.CheckboxInput( attrs = { 'class' : '' } ),
            'is_auto_increment': forms.CheckboxInput( attrs = { 'class' : '' } ),
            'is_unique'        : forms.CheckboxInput( attrs = { 'class' : '' } ),
            'is_primary_key'   : forms.CheckboxInput( attrs = { 'class' : '' } ),
            'is_indice'        : forms.CheckboxInput( attrs = { 'class' : '' } ),
            'register'         : forms.DateTimeField( disabled = True ),
            'last_update'      : forms.DateTimeField( disabled = True )
        }
"""
# TODO ver que es mas conveniente para Relationship

