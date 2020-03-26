from django.shortcuts import render,redirect,render_to_response
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from aula_virtual.apps.seguridad.models import Usuario
from random import shuffle, random
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.

#----Crud de Anexos

def Opcion(request):
    if 'usuario' in request.session:
        model = Opciones
        consulta = model.objects.filter(estado='ACTIVO',autor=request.session.get('usuario'))
        template_name = 'opciones/opciones.html'
        return render(request,template_name,{'opc':consulta})
    else:
        return redirect('seguridad:iniciar_sesion')



class AddOpciones(CreateView):
    model = Opciones
    form_class = formOpciones
    template_name = 'opciones/agregar_opciones.html'
    success_url = reverse_lazy('evaluacion:opciones')


class EditOpciones(UpdateView):
    model = Opciones
    form_class = formOpciones
    template_name = 'opciones/agregar_opciones.html'
    success_url = reverse_lazy('evaluacion:opciones')


def eliminar_opciones(request, id):
    opcion = Opciones.objects.get(id_opcion=id)
    try:
        if request.method == 'POST':
            opcion.estado = 'INACTIVO'
            opcion.save()
            return redirect('evaluacion:opciones')

    except Exception as e:
        return render(request, 'opciones/eliminar_opciones.html', {'error': e})

    return render(request, 'opciones/eliminar_opciones.html', {'opcion': opcion})


#----Crud de Anexos

def Preguntas(request):
    if 'usuario' in request.session:
        model = Pregunta
        consulta = model.objects.filter(estado='ACTIVO',autor=request.session.get('usuario'))
        template_name = 'pregunta/preguntas.html'
        return render(request,template_name,{'preguntas':consulta})
    else:
        return redirect('seguridad:iniciar_sesion')

class Addpreguntas(CreateView):
    model = Pregunta
    form_class = formPreguntas
    template_name = 'pregunta/agregar_pregunta.html'
    success_url = reverse_lazy('evaluacion:preguntas')


class EditPreguntas(UpdateView):
    model = Pregunta
    form_class = formPreguntas
    template_name = 'pregunta/agregar_pregunta.html'
    success_url = reverse_lazy('evaluacion:preguntas')


def eliminar_preguntas(request, id):
    pregunta = Pregunta.objects.get(id_pregunta=id)
    try:
        if request.method == 'POST':
            pregunta.estado = 'INACTIVO'
            pregunta.save()
            return redirect('evaluacion:preguntas')

    except Exception as e:
        return render(request, 'pregunta/eliminar_pregunta.html', {'error': e})

    return render(request, 'pregunta/eliminar_pregunta.html', {'pregunta': pregunta})

#----Crud de Examenes

def Examenes(request):
    if 'usuario' in request.session:
        model = Examen
        consulta = model.objects.filter(estado='ACTIVO',autor=request.session.get('usuario'))
        template_name = 'examenes/examenes.html'
        return render(request,template_name,{'examenes':consulta})

class AddExamenes(CreateView):
    model = Examen
    form_class = formExamen
    template_name = 'examenes/agregar_examenes.html'
    success_url = reverse_lazy('evaluacion:examenes')


class EditExamenes(UpdateView):
    model = Examen
    form_class = formExamen
    template_name = 'examenes/agregar_examenes.html'
    success_url = reverse_lazy('evaluacion:examenes')


def eliminar_examenes(request, id):
    examen = Examen.objects.get(id_examen=id)
    try:
        if request.method == 'POST':
            examen.estado = 'INACTIVO'
            examen.save()
            return redirect('evaluacion:examenes')

    except Exception as e:
        return render(request, 'examenes/eliminar_examenes.html', {'error': e})

    return render(request, 'examenes/eliminar_examenes.html', {'examen': examen})


def realizar_examen(request,id):
    contexto = {}
    lista_anexo = []
    examen = Examen.objects.get(id_examen=id)
    preguntas = list(Pregunta.objects.filter(examen_id__id_examen= id)[:10])
    contexto['examen'] = examen
    contexto['lista_anexos']: lista_anexo
    contexto['preguntas'] = preguntas
    total = 10

    if request.method == 'POST':
        for p in preguntas:
            opcion = request.POST.get('pregunta_{}'.format(p.id_pregunta))
            if opcion == None:
                opcion = 0
            for o in p.opciones.filter(respuesta = 'CORRECTA'):
                if o.id_opcion == int(opcion):
                    break
                else:
                    total = total - 1

        if total >= 7:
            contexto['mensaje_de_felicitaciones'] = 'Excelente amigo!! tus nota es:{} !'.format(total)
            return render(request, 'realizar_examen/realizar_examen.html', contexto)

        else:
            #print(lista_anexo)
            contexto['aciertos'] = total
            contexto['mensaje_de_error'] = total


            return render(request, 'realizar_examen/realizar_examen.html', contexto)

    return render(request,'realizar_examen/realizar_examen.html',contexto)
