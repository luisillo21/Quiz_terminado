from django.db.models import Q
from django import forms
from django.forms import ModelForm

from aula_virtual.apps.seguridad.models import Usuario
from aula_virtual.apps.seguridad.context_processors import permisos
from django.http import request

from .models import *

class formMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = [
            "descripcion",
            ]

        labels = {
            "descripcion" : "Materia",
        }

        widgets = {
            "descripcion": forms.TextInput(attrs={"class": "form-control", "placeholder":"ingrese el nombre de la materia"}),
        }

class formExamen(forms.ModelForm):
    class Meta:
        model = Examen
        fields = [
            "nombre",
            "id_materia",
            "descripcion",
            "autor",
            ]

        labels = {
            "nombre" : "Nombre",
            "id_materia" : "Materia",
            "descripcion" : "Descripcion",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder":"ingrese el nombre del examen"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control", "placeholder": "ingrese el nombre del examen"}),
        }


class formOpciones(forms.ModelForm):
    class Meta:
        model = Opciones
        fields = [
            "descripcion",
            "autor",
            "respuesta",
            ]

        labels = {
            "descripcion" : "Opcion",
            "autor" : "Autor",
            "respuesta" : "Esta opcion es la respuesta correcta?"
        }

        widgets = {
            "descripcion": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese la opcion"}),
        }

class formPreguntas(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            "pregunta",
            "autor",
            "examen",
            "opciones",
            ]

        labels = {
            "pregunta" : "Pregunta",
        }

        widgets = {
            "pregunta": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese la pregunta"}),
            "anexo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el material relacionaro"}),
        }



