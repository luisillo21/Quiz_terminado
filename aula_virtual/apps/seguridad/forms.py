from django import forms
from django.forms import ModelForm

from .models import *


class formPermisos(forms.ModelForm):
    class Meta:
        model = Permisos
        fields = [
            "rol",
            "menu",
            ]

        labels = {
            "rol" : "Rol",
            "menu" : "Menu",
        }

class formPersonas(forms.ModelForm):
    class Meta:
        model = Personas
        fields = [
            "nombres",
            "apellidos",
            "cedula",
            "foto",
            ]

        labels = {
            "nombres" : "Nombre",
            "apellidos" : "Apellidos",
            "cedula" : "Cedula",
            "foto" : "Foto de perfil",
        }

class formUsuarios(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "usuario",
            "correo",
            "clave",
            "id_persona",
            "rol_usuario",
            ]

        labels = {
            "usuario" : "Nombre de usuario",
            "clave" : "Contraseña",
            "correo" : "Correo de esta cuenta",
            "id_persona":"Persona",
            "rol_usuario":"Rol de este usuario"
        }

        widgets = {
            "clave": forms.TextInput(attrs={"class": "form-control", "type": "password"}),
        }
    
 