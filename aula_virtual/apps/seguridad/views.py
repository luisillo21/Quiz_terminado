from django.shortcuts import render,redirect,render_to_response
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.http import HttpResponseRedirect, HttpResponse

from aula_virtual.apps.evaluacion.models import Examen
from .models import *
from .forms import *
from django.urls import reverse_lazy
import hashlib
# Create your views here.


def inicio(request):
     if 'usuario' in request.session:
         return render(request, 'index.html')
     else:
        return redirect('seguridad:inicio_quiz')

def inicio_quiz(request):
    if 'usuario' in request.session:
        return redirect('seguridad:inicio')
    else:
        consulta = Examen.objects.all()
        return render(request,'inicio.html',{'examenes':consulta})

def login(request):
    contexto = {}
    try:
        if request.method == 'POST':
            var_usuario = request.POST.get('usu')
            var_contra = request.POST.get('pass')            
            usu = Usuario.objects.get(usuario=var_usuario, clave=var_contra, estado='ACTIVO')
            if usu:
                request.session['usuario'] = usu.id_usuario
                return redirect("seguridad:inicio") 
    except Exception as e:
        contexto['error'] = "Usuario o contraseña incorrectos"
        return render(request, 'Login.html', contexto)
    return render(request,'Login.html')

def salir(request):
    del request.session['usuario']
    return redirect('seguridad:inicio')

#-- CRUD DE PERSONAS------------------------------------------------------------------

class Persona(ListView):
    model = Personas
    queryset = model.objects.filter(estado='ACTIVO')
    template_name = 'personas/personas.html'

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['per'] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if 'usuario' in request.session:
            return render(request, self.template_name, self.get_context_data())
        else:
            return redirect('seguridad:iniciar_sesion')

class AddPersona(CreateView):
    model = Personas
    form_class = formPersonas
    template_name = 'personas/agregar_personas.html'
    success_url = reverse_lazy('seguridad:personas')

class EditPersona(UpdateView):
    model = Personas
    form_class = formPersonas
    template_name = 'personas/agregar_personas.html'
    success_url = reverse_lazy('seguridad:personas')

def eliminar_persona(request,id):
    persona = Personas.objects.get(id_persona=id)
    try:
        if request.method == 'POST':
           persona.estado = 'INACTIVO'
           persona.save()
           return redirect('seguridad:personas')

    except Exception as e:
        return render(request, 'personas/eliminar_personas.html', {'error':e})

    return render(request,'personas/eliminar_personas.html',{'personas':persona})

#-- CRUD DE USUARIO-----------------------------------------------------------------

class Usuario_listar(ListView):
    model = Usuario
    context_object_name = 'usuario'
    queryset = model.objects.filter(estado='ACTIVO')
    template_name = 'usuarios/usuarios.html'

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['usuario'] = self.get_queryset()
        return contexto

    def get(self, request, *args, **kwargs):
        if 'usuario' in request.session:
            return render(request, self.template_name, self.get_context_data())
        else:
            return redirect('seguridad:iniciar_sesion')

class AddUsuario(CreateView):
    model = Usuario
    form_class = formUsuarios
    template_name = 'usuarios/agregar_usuarios.html'
    success_url = reverse_lazy('seguridad:usuarios')

class EditUsuario(UpdateView):
    model = Usuario
    form_class = formUsuarios
    template_name = 'usuarios/agregar_usuarios.html'
    success_url = reverse_lazy('seguridad:usuarios')

def eliminar_usuario(request,id):
    usuario = Usuario.objects.get(id_usuario=id)
    try:
        if request.method == 'POST':
           usuario.estado = 'INACTIVO'
           usuario.save()
           return redirect('seguridad:usuarios')

    except Exception as e:
        return render(request, 'usuarios/eliminar_usuarios.html', {'error':e})

    return render(request,'usuarios/eliminar_usuarios.html',{'usuario':usuario})