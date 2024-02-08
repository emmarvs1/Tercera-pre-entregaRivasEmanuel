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
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    
def __str__(self):
        return self.nombre
    
    