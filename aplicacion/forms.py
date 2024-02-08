from django import forms   

class PizzaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)


class EmpanadasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class BebidasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)    
    
class ClientesForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True, label="Cuenta de Correo")
    comentario = forms.CharField(max_length=150, required=True)