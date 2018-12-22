from django.db import models

# Create your models here.
class Proyect( models.Model ):

    name        = models.CharField( unique = True, max_length = 300 )
    register    = models.DateTimeField( auto_now = True )
    last_update = models.DateTimeField( auto_now = True )


class Entity( models.Model ):

    id_proyect  = models.ForeignKey( Proyect, on_delete = models.CASCADE )
    name        = models.CharField( unique = True, max_length = 300 )
    register    = models.DateTimeField( auto_now = True )
    last_update = models.DateTimeField( auto_now = True )

class Attribute( models.Model ):

    # TODO Agregar todas los tipos de datos que se aseptaran
    # si no buscar otra estrategia
    TYPE_DB = (
        ( 1, 'BigInt' ),
        ( 2, 'Int' )
    )

    id_entity         = models.ForeignKey( Entity, on_delete = models.CASCADE )
    name              = models.CharField( unique = True, max_length = 150 )
    type              = models.CharField( choices = TYPE_DB, max_length = 150 )
    is_null           = models.BinaryField( default = False )
    is_auto_increment = models.BinaryField( default = False )
    is_unique         = models.BinaryField( default = False )
    is_primary_key    = models.BinaryField( default = False )
    is_indice         = models.BinaryField( default = False )
    register          = models.DateTimeField( auto_now = True )
    last_update       = models.DateTimeField( auto_now = True )

class Relationship( models.Model ):

    name                  = models.CharField( unique = True, max_length = 200 )
    attribute_foreign_key = models.CharField( max_length = 150 )
    entity_reference      = models.CharField( max_length = 150 )
    attribute_reference   = models.CharField( max_length = 150 )
    register              = models.DateTimeField( auto_now = True )
    last_update           = models.DateTimeField( auto_now = True )


