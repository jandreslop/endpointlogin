from django.db import models


class NombreUsuario(models.Model):
    user_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user_name


class Login(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=55)
    mail = models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)
    NombreUsuario = models.ForeignKey(NombreUsuario, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.nombre
    




# Create your models here.
