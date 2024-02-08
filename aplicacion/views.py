from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def ver_pizzas(request):
    contexto = {'pizzas': Pizza.objects.all()}
    return render(request, "aplicacion/pizzas.html", contexto)

def ver_empandas(request):
    contexto = {'empanadas': EmpanadasForm.objects.all()}
    return render(request, "aplicacion/empanadas.html", contexto)

def ver_bebidas(request):
    return render(request, "aplicacion/bebidas.html")

def ver_clientes(request):
    return render(request, "aplicacion/clientes.html")

def ver_pizzaForm(request):
    if request.method == "POST":
        miFormulario = PizzaForm(request.POST)  
        if miFormulario.is_valid():
            pizza_nombre = miFormulario.cleaned_data.get("pizza")
            pizza_precio = miFormulario.cleaned_data.get("precio")
            precio = Pizza(nombre=pizza_nombre, precio=pizza_precio)  
            precio.save()
            return render(request, "aplicacion/home.html")


    else:    
        miFormulario = PizzaForm()

    return render(request, "aplicacion/pizzaForm.html", {"form": miFormulario})

def ver_empanadasForm(request):
    if request.method == "POST":
        miForm = EmpanadasForm(request.POST)
        if miForm.is_valid():
            empanada_nombre = miForm.cleaned_data.get("empanada")
            empanada_precio = miForm.cleaned_data.get("precio")
            empanada = Empanadas(nombre=empanada_nombre, empanada_precio=empanada_precio)
            empanada.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = EmpanadasForm()

    return render(request, "aplicacion/empanadasForm.html", {"form": miForm })    

def buscar(request):
    return render(request, "aplicacion/buscarPizzas.html")

def ver_clientes(request):
    if request.method == "POST":
        miForm = ClientesForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente_comentario = miForm.cleaned_data.get("comentario")
            cliente = Clientes(nombre=cliente_nombre, apellido=cliente_apellido,
                            email=cliente_email, comentario=cliente_comentario)
            cliente.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = ClientesForm()

    return render(request, "aplicacion/clientesForm.html", {"form": miForm })

def buscarPizzas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        pizzas = buscarPizzas.objects.filter(nombre__icontains=patron)
        contexto = {"pizzas": pizzas }
        return render(request, "aplicacion/pizzas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")
