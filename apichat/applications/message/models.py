from django.db import models
# from django.contrib.auth.models import User
from applications.users.models import User
from model_utils.models import TimeStampedModel
# Create your models here.
class Message(TimeStampedModel):
    """  Modelo para registrar Mensajes de un Usuario  """

    message = models.CharField(
        'Mensaje', 
        max_length=300,
    )
    image = models.CharField(
        'Imagen', 
        blank=True, 
        null=True,
        max_length=300,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    active  = models.BooleanField(
        blank=True, 
        null=True,
        default=True,
    )


    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.message