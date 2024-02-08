from django.db import models

# Create your models here.
class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
def __str__(self):
        return f"{self.nombre}"

class Bebidas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
def __str__(self):
        return f"{self.nombre}"    

class Empanadas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
def __str__(self):
        return f"{self.nombre}"
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    comentario = models.TextField()
    
def __str__(self):
        return self.nombre
    
    
    