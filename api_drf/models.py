from django.db import models

# Create your models here.


class User_DRF(models.Model):
    """
    Modelo base para la API Rest basada en DRF
    """
    name_drf = models.CharField(max_length=100)
    email_drf = models.EmailField(max_length=250)
    
