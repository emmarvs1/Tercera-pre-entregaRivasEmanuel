from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name="home"),
    path('pizzas/', ver_pizzas, name="pizzas"),
    path('empanadas/', ver_empandas, name="empanadas"),
    path('bebidas/', ver_bebidas, name="bebidas"),
    path('clientes/', ver_clientes, name="clientes"),
        
    path('pizza_form/', PizzaForm, name="pizza_form"),
    path('empanadas_form/', ver_empanadasForm, name="empanadas_form"),
    
    path('buscarPizzas/', buscarPizzas, name="buscarPizzas"),
    path('buscar/', buscar, name="buscar"),
]
