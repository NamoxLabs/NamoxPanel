from django.db import models

from namoxpanel.userprofile.models import User

# Create your models here.
class Project(models.Model):
    name        = models.CharField( unique = True, max_length = 300 )
    created_by  = models.ForeignKey( User, related_name='project_creator', on_delete = models.CASCADE )
    created_at  = models.DateTimeField( auto_now = True )
    last_update = models.DateTimeField( auto_now = True )


class Entity( models.Model ):
    project     = models.ForeignKey( Project, related_name='project_entity', on_delete = models.CASCADE )
    name        = models.CharField( unique = True, max_length = 300 )
    created_by  = models.ForeignKey( User, related_name='entity_creator', on_delete = models.CASCADE )
    updated_by  = models.ForeignKey( User, related_name='entity_update_user', on_delete = models.CASCADE )
    created_at  = models.DateTimeField( auto_now = True )
    last_update = models.DateTimeField( auto_now = True )


class Attribute( models.Model ):
    # TODO Agregar todas los tipos de datos que se aseptaran
    # si no buscar otra estrategia
    TYPE_DB = (
        ( 1, 'BigInt' ),
        ( 2, 'Int' )
    )

    entity            = models.ForeignKey( Entity, related_name='entity_attribute', on_delete = models.CASCADE )
    name              = models.CharField( unique = True, max_length = 150 )
    type              = models.CharField( choices = TYPE_DB, max_length = 150 )
    is_null           = models.BinaryField( default = False )
    is_auto_increment = models.BinaryField( default = False )
    is_unique         = models.BinaryField( default = False )
    is_primary_key    = models.BinaryField( default = False )
    is_index          = models.BinaryField( default = False )
    created_by        = models.ForeignKey( User, related_name='user_creation', on_delete = models.CASCADE )
    updated_by        = models.ForeignKey( User, related_name='user_update', on_delete = models.CASCADE )
    created_at        = models.DateTimeField( auto_now = True )
    last_update       = models.DateTimeField( auto_now = True )

"""
class Relationship( models.Model ):

    name                  = models.CharField( unique = True, max_length = 200 )
    attribute_foreign_key = models.CharField( max_length = 150 )
    entity_reference      = models.CharField( max_length = 150 )
    attribute_reference   = models.CharField( max_length = 150 )
    created_at            = models.DateTimeField( auto_now = True )
    last_update           = models.DateTimeField( auto_now = True )
"""