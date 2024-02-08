from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('pizzas/', ver_pizzas, name="pizzas"),
    path('empanadas/', ver_empandas, name="empanadas"),
    path('bebidas/', ver_bebidas, name="bebidas"),
    path('clientes/', ver_clientes, name="clientes"),
        
    path('pizza_form/', ver_pizzaForm, name="pizza_form"),
    path('empanadas_form/', ver_empanadasForm, name="empanadas_form"),
    
    path('buscar/', buscar, name="buscar"),
    path('buscarPizzas/', buscarPizzas, name="buscarPizzas"),
]