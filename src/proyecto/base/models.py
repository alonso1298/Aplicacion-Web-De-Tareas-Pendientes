from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE, #CASCADE indica que si el usuario es eliminado, elimina cualquier tarea de este mismo
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateField(auto_now_add=True) #Se genera automaticamente la hora y la fecha de creación

    def __str__(self):
        return self.titulo
    
    class Meta:
        #Las tareas que estan compretas se van al fondo de la lista
        ordering = ['completo'] 