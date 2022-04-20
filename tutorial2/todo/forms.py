from django import forms 

class AgregarTarea(forms.Form):
    tarea = forms.CharField()#esto es para especificar que tipo de dato se va a ingresar

