from django.db import models

from namoxpanel.userprofile.models import User

class Database(models.Model):
    name = models.CharField(
        unique = True, 
        max_length = 300)
    created_by = models.ForeignKey(
        User, 
        related_name='database_creator',
        null=True, blank=True,
        on_delete=models.CASCADE)
    created_at = models.DateTimeField( 
        auto_now=True)
    last_update = models.DateTimeField(
        auto_now=True)


class Entity(models.Model):
    database = models.ForeignKey(
        Database, 
        related_name='project_entity', 
        null=True, blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(
        unique=True, 
        max_length=300)
    created_by = models.ForeignKey(
        User, 
        related_name='entity_creator',
        on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User,
        related_name='entity_update_user',
        on_delete = models.CASCADE)
    created_at  = models.DateTimeField(
        auto_now = True)
    last_update = models.DateTimeField(
        auto_now = True)


class Attribute(models.Model):
    TYPE_DB = (
        ( 1, 'BigInt' ),
        ( 2, 'Int' )
    )
    entity            = models.ForeignKey(Entity, related_name='entity_attribute', on_delete = models.CASCADE)
    name              = models.CharField(unique = True, max_length = 150)
    type              = models.CharField(choices = TYPE_DB, max_length = 150)
    is_null           = models.BinaryField(default = False)
    is_auto_increment = models.BinaryField(default = False)
    is_unique         = models.BinaryField(default = False)
    is_primary_key    = models.BinaryField(default = False)
    is_index          = models.BinaryField(default = False)
    created_by        = models.ForeignKey(User, related_name='user_creation', on_delete = models.CASCADE)
    updated_by        = models.ForeignKey(User, related_name='user_update', on_delete = models.CASCADE)
    created_at        = models.DateTimeField(auto_now = True)
    last_update       = models.DateTimeField(auto_now = True)
