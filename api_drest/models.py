import json
from django.db import models

# Create your models here.

class User_Rest(models.Model):
    """
    Modelo base API Rest sin uso de DRF
    """
    name_drest = models.CharField('Nombre',max_length=100)
    email_drest = models.EmailField('Email',max_length=250)


    def serialize_user(id):
        """
        Convierte el Objeto por el que se consulta en formato JSON
        """
        user_drest = User_Rest.objects.get(id=id)
        return json.dumps({'id':user_drest.id,'email':user_drest.email_drest,'name':user_drest.name_drest})

